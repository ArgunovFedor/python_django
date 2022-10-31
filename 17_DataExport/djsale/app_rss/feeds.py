from typing import List

from django.contrib.syndication.views import Feed
from django.db.models import QuerySet
from django.urls import reverse

from app_housing.models import Housing
from app_news.models import NewsItem


class LatestNewsFeed(Feed):
    title = 'Новости'
    link = '/sitenews/'
    description = 'Самые свежие новости'

    def items(self) -> QuerySet:
        return NewsItem.objects.order_by('-published_at')[:10]

    def item_title(self, item: NewsItem) -> str:
        return item.title

    def item_description(self, item: NewsItem) -> str:
        return item.description

    def item_link(self, item: NewsItem) -> str:
        return reverse('news-item', args=[item.pk])


class LatestHousing(Feed):
    title = 'Жилье'
    link = '/sitenewshousing/'
    description = 'Новое жилье'

    def items(self) -> QuerySet:
        return Housing.objects.order_by('-published_at')[:10]

    def item_title(self, item: Housing) -> str:
        return Housing.name

    def item_description(self, item: Housing) -> List[str]:
        return ' '.split([Housing.name, Housing.price, Housing.type_of_house, Housing.published_at])

    def item_link(self, item: NewsItem) -> str:
        return reverse('housing-item', args=[item.pk])