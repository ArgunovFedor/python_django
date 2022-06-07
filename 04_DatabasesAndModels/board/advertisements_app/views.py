import random

from django.shortcuts import render
from advertisements_app.models import Advertisement, News, Comments
from django.views.generic import ListView, DetailView, CreateView, UpdateView


def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    advertisement = advertisements[random.randint(0, len(advertisements) - 1)]
    return render(request, 'advertisements/advertisement_list.html', {
        'advertisements': advertisements,
        'random_advertisement': advertisement
    })


class AdvertisementListView(ListView):
    template_name = 'advertisements/advertisement_list.html'
    model = Advertisement
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(DetailView):
    template_name = 'advertisements/advertisement_detail.html'
    model = Advertisement
    context_object_name = 'advertisement_detail'


class NewsListView(ListView):
    template_name = 'news/news_list.html'
    model = News
    context_object_name = 'news_list'
    queryset = News.objects.filter(is_active=True).order_by('created_at')


class NewsListDetailView(DetailView):
    template_name = 'news/news_detail.html'
    model = News
    context_object_name = 'news_detail'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(NewsListDetailView, self).get_context_data(**kwargs)
        context['comment_list'] = Comments.objects.filter(news_id=pk)
        return context


class NewsCreateView(CreateView):
    template_name = 'news/news_create.html'
    model = News
    fields = ['name', 'content', 'is_active']


class NewsUpdateView(UpdateView):
    template_name = 'news/news_update.html'
    model = News
    fields = ['name', 'content', 'is_active']


class CommentsCreateView(CreateView):
    template_name = 'comments/comments_create.html'
    model = Comments
    fields = ['username', 'text']

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        form.instance.news_id = pk
        return super().form_valid(form)


class CommentsListView(ListView):
    template_name = 'comments/comments_list.html'
    model = Comments
    context_object_name = 'comments_list'


class CommentsListDetailView(DetailView):
    template_name = 'comments/comments_detail.html'
    model = Comments
    context_object_name = 'comments_detail'
