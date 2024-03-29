from django.urls import path
from app_goods.views import ItemList, ItemDetail

urlpatterns = [
    path('items/', ItemList.as_view(), name='items_list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='items_detail')
]