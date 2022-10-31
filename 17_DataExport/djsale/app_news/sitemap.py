from django.contrib.sitemaps import Sitemap

from app_housing.models import Housing
from app_news.models import NewsItem


class NewsSitemap(Sitemap):
    # частота измения страниц с постами
    changefreq = 'weekly'
    # релеватность на сайте
    priority = 0.9

    def items(self):
        return NewsItem.objects.filter(is_published=True).all()

    def lastmod(self, obj: NewsItem):
        return obj.published_at


class HousingSitemap(Sitemap):
    # частота измения страниц с постами
    changefreq = 'weekly'
    # релеватность на сайте
    priority = 0.9

    def items(self):
        return Housing.objects.all()

    def lastmod(self, obj: Housing):
        return obj.published_at
