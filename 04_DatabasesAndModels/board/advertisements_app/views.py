import random

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from advertisements_app.models import Advertisement, News, Comments
from advertisements_app.forms import AuthForm
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
    fields = ['username', 'text', 'boy']

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        if isinstance(self.request.user, User):
            form.instance.user = self.request.user
        form.instance.news_id = pk
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CommentsCreateView, self).get_form_kwargs()
        return kwargs


class CommentsListView(ListView):
    template_name = 'comments/comments_list.html'
    model = Comments
    context_object_name = 'comments_list'


class CommentsListDetailView(DetailView):
    template_name = 'comments/comments_detail.html'
    model = Comments
    context_object_name = 'comments_detail'


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class AnotherLogoutView(LogoutView):
    next_page = '/'


def login_view(request):
    if request.method == 'POST': # Для POST пытаемся аутентифицировать пользователя
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if True:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect(redirect_to='/')
                    else:
                        auth_form.add_error('__all__', 'Ошибка. Учетная запись пользователя не активна')
                else:
                    auth_form.add_error('__all__', 'Ошибка. Сайт работает с 8 до 20')
            else:
                auth_form.add_error('__all__','Ошибка! проверьте написания логина и пароля')
    else: # Для всех остальных запросов просто отображаем саму страничку логина
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'users/login.html', context=context)
