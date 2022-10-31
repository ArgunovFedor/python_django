from django.urls import path
from app_news.views import get_news_in_custom_format, NewsItemDetailView, NewsItemsView

urlpatterns = [
    path('', get_news_in_custom_format, name='news_list'),
    path('<int:pk>', NewsItemDetailView.as_view(), name='news-item'),
    path('news', NewsItemsView.as_view(), name='news'),
]
