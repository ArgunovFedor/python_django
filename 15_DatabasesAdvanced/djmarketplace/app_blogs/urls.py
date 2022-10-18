from django.contrib import admin
from django.urls import path
from app_blogs.views import publish_blog_post

urlpatterns = [
    path('publish/<int:user_id>/<int:scope_values>/', publish_blog_post, name='publish'),
]
