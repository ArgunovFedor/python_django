from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from app_users.forms import AuthForm, RegisterForm, EditAccountForm, RestorePasswordForm
from app_users.models import Profile


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class AnotherLogoutView(LogoutView):
    next_page = '/'


@permission_required('app_users.view_users')
def edit_account_view(request):
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = EditAccountForm()
    return render(request, 'users/edit_account.html', {'form': form})


@permission_required('app_users.view_users')
def account_view(request):
    return render(request, 'users/account.html')


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


def restore_password(request):
    if request.method == 'POST':
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            new_password = User.objects.make_random_password()
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
            send_mail(
                subject='Восстановление пароля',
                message='Test',
                from_email='admin@company.com',
                recipient_list=[form.cleaned_data['email']]
            )
            return HttpResponse('Письмо с первым паролем было успешно отправлено')
    restore_password_form = RestorePasswordForm()
    context = {
        'form': restore_password_form
    }
    return render(request, 'users/restore_password.html', context=context)
