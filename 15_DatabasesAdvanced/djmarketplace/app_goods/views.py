from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect

from app_goods.forms import ItemForm, ShoppingCartForm, ItemsForm, GoodForm
from app_goods.models import Item, ShoppingCart
from app_goods.utils import add_to_shopping_card, MyCustomException, define_total_summ_and_description, \
    confirm_the_order

@transaction.atomic
def items_list_view(request):
    # пагинацию не реализовал намеренно
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data.get('id')
            # Из основной страницы просто добавляет 1 товар.
            # А конкретно количество из самой корзины
            add_to_shopping_card(user_id=request.user.id, item_id=item_id, count=1)
    items_list = Item.objects.all()
    is_have_card = ShoppingCart.objects.filter(user=request.user).exists()
    if not is_have_card:
        context = {
            'items_list': items_list,
            'card_count': 0
        }
        return render(request, 'goods/items_list.html', context=context)
    context = {
        'items_list': items_list,
        'card_count': ShoppingCart.objects.filter(user=request.user).count()
    }
    return render(request, 'goods/items_list.html', context=context)


@transaction.atomic
def shopping_cart_view(request):
    error_list = {}
    if request.method == 'POST':
        item_id = int(request.POST['id'])
        count = int(request.POST['count'])
        try:
            add_to_shopping_card(request.user.id, item_id, count)
        except MyCustomException as err:
            error_list[err.id] = err

    is_have_shopping_cart = ShoppingCart.objects.filter(user_id=request.user.id).exists()
    context = {}
    if is_have_shopping_cart:
        carts = ShoppingCart.objects.select_related('items').filter(user_id=request.user.id)
        shopping_cart_forms = []
        for cart in carts:
            # в случае, если возникла ошибка. Например, количество больше, чем в магазине
            if cart.id in error_list:
                shopping_cart = ShoppingCartForm(request.POST)
                shopping_cart.add_error('count', error_list[cart.id])
            else:
                shopping_cart = ShoppingCartForm(instance=cart)
            shopping_cart_forms.append(
                {
                    'shopping_card_form': shopping_cart,
                    'items_form': ItemsForm(instance=cart.items),
                    'description': GoodForm(instance=cart.items.code)
                }
            )
        error_list = {}
        context = {
            'shopping_carts': shopping_cart_forms
        }
    return render(request, 'goods/shopping_card.html', context=context)


@transaction.atomic
def form_payment_view(request):
    if request.method == 'POST':
        confirm_the_order(user_id=request.user.id)
        return redirect('/')
    total_summ, description = define_total_summ_and_description(user_id=request.user.id)
    context = {
        'total_summ': total_summ['total_summ'],
        'description': description
    }
    return render(request, 'goods/form_payment.html', context=context)