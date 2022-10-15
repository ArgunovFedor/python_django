import threading

from app_blogs.models import *
from app_users.models import *
from django.contrib.auth.models import User

def reduce_user_balance(user_id: int, scope_values: int):
    """
    Метод для повышения очков
    :param user_id:
    :param scope_values:
    :return:
    """
    user = User.objects.filter(id=user_id).first()
    #TODO: что-то UserPrifile не пашет так как надо
    profile = UserProfile.objects.filter(id=user.id).first()
    profile.score += scope_values
    if profile.status != 'Эксперт':
        if profile.score > 10000:
            profile.status = 'Эксперт'
        elif profile.score > 1000:
            profile.status = 'Продвинутый'


def publish_post(post_id):
    """
    Метод для публикации поста
    :return:
    """
    post = Post.objects.all()
    # TODO: сделать логику публикации поста
