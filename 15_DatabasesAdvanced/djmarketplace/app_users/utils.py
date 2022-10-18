from datetime import datetime

from app_users.models import *
from django.contrib.auth.models import User


def update_user_profile(user_id: int, city: str, date_of_birth: datetime):
    """
    Метод для обновления данных пользователя
    :param user_id: id пользователя
    :param city: город
    :param date_of_birth: день рождения
    :param status: статус
    :param balance: балансе
    :return:
    """
    user = User.objects.filter(id=user_id).first()
    profile = UserProfile.objects.filter(user=user.id).first()
    profile.city = city
    profile.date_of_birth = date_of_birth
    profile.save()


def update_balance(user_id: int, balance: int):
    """
    Обновляет баланс
    :param user_id:
    :param balance: на сколько нужно увеличить баланс
    :return:
    """
    user = User.objects.filter(id=user_id).first()
    profile = UserProfile.objects.filter(user=user.id).first()
    profile.balance += balance
    profile.save()

