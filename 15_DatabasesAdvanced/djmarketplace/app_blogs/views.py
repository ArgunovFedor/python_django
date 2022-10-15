from django.db import transaction
from django.shortcuts import render
from app_blogs.utils import reduce_user_balance, publish_post


@transaction.atomic
def publish_blog_post(post_id, user_id, scope_values):
    reduce_user_balance(user_id, scope_values)
    publish_post(post_id)
