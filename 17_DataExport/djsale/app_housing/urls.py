from django.urls import path
from app_housing.views import list_of_housing_for_sale, HousingDetailView, HousingItemsView

urlpatterns = [
    path('', list_of_housing_for_sale, name='housing_list'),
    path('<int:pk>', HousingDetailView.as_view(), name='housing-item'),
    path('house', HousingItemsView.as_view(), name='housing'),
]
