from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='categories_list'),
    path('advertisements', views.AdvertisementListView.as_view(), name='advertisements'),
    path('advertisements/<int:pk>', views.AdvertisementDetailView.as_view(), name='advertisements-detail'),
]
