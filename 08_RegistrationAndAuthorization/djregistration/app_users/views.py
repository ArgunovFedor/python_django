import random
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from app_users.forms import AuthForm, RegisterForm
from app_users.models import Profile, Advertisement, News, Comments


def login_view(request):
    if request.method == 'POST':  # Для POST пытаемся аутентифицировать пользователя
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if True:
                    if user.is_active and not user.is_superuser:
                        login(request, user)
                        return HttpResponseRedirect(redirect_to='/')
                    else:
                        auth_form.add_error('__all__', 'Ошибка. Учетная запись пользователя не активна')
                else:
                    auth_form.add_error('__all__', 'Ошибка. Сайт работает с 8 до 20')
            else:
                auth_form.add_error('__all__', 'Ошибка! проверьте написания логина и пароля')
    else:  # Для всех остальных запросов просто отображаем саму страничку логина
        auth_form = AuthForm()
    auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'users/login.html', context=context)


def logout_view(request):
    logout(request)
    return HttpResponse('Вы успешно вышли из своей учетной записи')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            row_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=row_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def another_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth
            )
            username = form.cleaned_data.get('username')
            row_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=row_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


@permission_required('app_users.view_users')
def account_view(request):
    return render(request, 'users/account.html')

@permission_required('app_users.view_advertisement')
def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    advertisement = advertisements[random.randint(0, len(advertisements) - 1)]
    return render(request, 'advertisements/advertisement_list.html', {
        'advertisements': advertisements,
        'random_advertisement': advertisement
    })



class AdvertisementListView(PermissionRequiredMixin, ListView):
    permission_required = 'app_users.view_advertisement'
    template_name = 'advertisements/advertisement_list.html'
    model = Advertisement
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]

class AdvertisementDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'app_users.view_advertisement'
    template_name = 'advertisements/advertisement_detail.html'
    model = Advertisement
    context_object_name = 'advertisement_detail'

class NewsListView(PermissionRequiredMixin, ListView):
    permission_required = 'app_users.view_news'
    template_name = 'news/news_list.html'
    model = News
    context_object_name = 'news_list'
    queryset = News.objects.filter(is_active=True).order_by('created_at')


class NewsListDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'app_users.view_news'
    template_name = 'news/news_detail.html'
    model = News
    context_object_name = 'news_detail'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(NewsListDetailView, self).get_context_data(**kwargs)
        context['comment_list'] = Comments.objects.filter(news_id=pk)
        return context

class NewsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'app_users.create_news'
    template_name = 'news/news_create.html'
    model = News
    # из филдов убрано active, чтобы модератор мог потом добавить эту новость
    fields = ['name', 'content']

class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_users.update_news'
    template_name = 'news/news_update.html'
    model = News
    fields = ['name', 'content', 'is_active']

class CommentsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'app_users.create_comments'
    template_name = 'comments/comments_create.html'
    model = Comments
    fields = ['username', 'text']

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        if isinstance(self.request.user, User):
            form.instance.user = self.request.user
        form.instance.news_id = pk
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CommentsCreateView, self).get_form_kwargs()
        return kwargs


class CommentsListView(PermissionRequiredMixin, ListView):
    permission_required = 'app_users.view_comments'
    template_name = 'comments/comments_list.html'
    model = Comments
    context_object_name = 'comments_list'


class CommentsListDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'app_users.view_comments'
    template_name = 'comments/comments_detail.html'
    model = Comments
    context_object_name = 'comments_detail'


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class AnotherLogoutView(LogoutView):
    next_page = '/'
