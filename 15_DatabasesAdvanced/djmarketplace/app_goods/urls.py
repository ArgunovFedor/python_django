from django.urls import path

from app_goods.views import items_list_view, shopping_cart_view, form_payment_view

urlpatterns = [
    path('items/', items_list_view, name='goods_items_list'),
    path('shopping_cart/', shopping_cart_view, name='shopping_cart'),
    path('form_payment/', form_payment_view, name='form_payment'),
    ]