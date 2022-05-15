from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='categories_list')
]
