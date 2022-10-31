from django.urls import path
from app_rss.feeds import LatestNewsFeed, LatestHousing

urlpatterns = [
    path('latest/feed', LatestNewsFeed()),
    path('latest/housing_feed', LatestHousing())
]
