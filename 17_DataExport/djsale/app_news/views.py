from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.views import generic

from app_news.models import NewsItem


def get_news_in_custom_format(request):
    format = request.GET['format']
    if format not in ['xml', 'json', 'yaml']:
        return HttpResponseBadRequest()
    data = serializers.serialize(format, NewsItem.objects.all())
    return HttpResponse(data)


class NewsItemDetailView(generic.DetailView):
    model = NewsItem
    template_name = 'news/news_detail.html'


class NewsItemsView(generic.ListView):
    model = NewsItem
    context_object_name = 'news_list'
    queryset = NewsItem.objects.all()[:5]
    template_name = 'news/news_list.html'
