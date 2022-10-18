import decimal

from django.contrib.auth.models import User
from django.db.models import Sum

from app_goods.models import ShoppingCart, Item
from app_users.models import UserProfile
from django.db.models import F


class MyCustomException(Exception):
    id = 0
    pass


def add_to_shopping_card(user_id: int, item_id: int, count: int):
    """
    Обновляет корзину
    :param item_id:
    :param user_id:
    :param balance: на сколько нужно увеличить баланс
    :return:
    """
    # В текущей реализации возможно добавить один и тот же товар в корзину
    # есть вариант просуммировать количество, но я решил не добавлять один и тот же
    # товар в корзину, если там уже есть. Если он есть, то обновляем на последнее
    # сделать так, чтобы количество товаров не должно было быть больше, чем в наличии в магазине
    item = Item.objects.get(pk=item_id)
    if item.count < count:
        shopping_card = ShoppingCart.objects.filter(items=item).first()
        exception = MyCustomException('В магазине нет в наличии столько товаров')
        exception.id = shopping_card.id
        raise exception

    user = User.objects.get(pk=user_id)
    is_there_product = ShoppingCart.objects.filter(user=user, items=item).exists()
    if not is_there_product:
        ShoppingCart.objects.create(user=user, count=count, items=item)
    else:
        shopping_card = ShoppingCart.objects.filter(items=item, user=user).first()
        # Если в корзине другое количество, а потом в общей списке выбрал тот же
        # товар, то количество будет равно 1
        shopping_card.count = count
        shopping_card.save(update_fields=['count'], force_update=True)


def define_total_summ_and_description(user_id: int):
    shopping_card_list = ShoppingCart.objects.select_related('items').filter(user_id=user_id)
    total_summ = shopping_card_list.annotate(summ=F('count') * F('items__price')).aggregate(total_summ=Sum('summ'))
    description = []
    for cart in shopping_card_list:
        description.append(f'{cart.items.code.name} - {cart.items.price}')
    return total_summ, description


def confirm_the_order(user_id: int):
    """
    В самую последнюю очередь нужно подтвердить заказ.
    Нужно проверить хватает ли денег у пользователя
    затем очистить корзину
    :param user_id:
    :return:
    """
    # делаем то же самое, что и define_total_summ_and_description
    # чтобы обезопасить процесс
    user = User.objects.get(pk=user_id)
    shopping_card_list = ShoppingCart.objects.select_related('items').filter(user=user)
    # общая сумма
    summ = shopping_card_list.annotate(summ=F('count') * F('items__price')).aggregate(total_summ=Sum('summ'))['total_summ']
    profile = UserProfile.objects.filter(user=user).first()
    if summ > profile.balance:
        delta = summ - profile.balance
        raise MyCustomException(f'Не достаточно денег. Не хватает - {delta}')
    list_items_to_update = []
    for card in shopping_card_list:
        # формируем список для обновления количества товаров в магазине
        card.items.count -= card.count
        if card.items.count <= 0:
            raise MyCustomException(
                f'Наличие товаров в магазине изменилось. Обновите количество {card.items.code.name}')
        list_items_to_update.append(card.items)
    # обновляем количества товаров в магазине
    Item.objects.bulk_update(list_items_to_update, ['count'])
    buy(profile=profile, summ=summ)
    profile.balance -= summ
    # опустошаем корзину
    ShoppingCart.objects.filter(user=user).delete()


def buy(profile: UserProfile, summ: decimal):
    profile.balance -= summ
    if decimal != 'Эксперт':
        if summ > 10000:
            profile.status = 'Эксперт'
        elif summ > 1000:
            profile.status = 'Продвинутый'
    profile.save()
