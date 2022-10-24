from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from app_users.forms import AuthForm, RegisterForm, RestorePasswordForm, EditAccountForm, ProfileForm, UpdateBalanceForm
from app_users.models import UserProfile
from app_users.utils import update_user_profile, update_balance

import logging

logger = logging.getLogger(__name__)

class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class AnotherLogoutView(LogoutView):
    next_page = '/'


#@permission_required('users.view_users', login_url='login')
@transaction.atomic
def edit_account_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            update_user_profile(user_id=request.user.id, city=city, date_of_birth=date_of_birth)
            return HttpResponseRedirect(reverse('account'))
    else:
        if request.user.id:
            user = User.objects.get(pk=request.user.id)
            form = EditAccountForm(instance=user)
            if hasattr(user, 'userprofile'):
                user_profile = UserProfile.objects.get(user=user)
                user_profile_form = ProfileForm(instance=user_profile)
            else:
                user_profile_form = ProfileForm()
    context = {
        'form': form,
        'user_profile_form': user_profile_form
    }
    return render(request, 'users/edit_account.html', context)


# @permission_required('users.view_users', login_url='login')
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
                if user.is_active:
                    login(request, user)
                    logger.info(f'Пользователь {user} аутентифицировался')
                    return HttpResponseRedirect(redirect_to='/')
                else:
                    auth_form.add_error('__all__', 'Ошибка. Учетная запись пользователя не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка! проверьте написания логина и пароля')
    else:  # Для всех остальных запросов просто отображаем саму страничку логина
        auth_form = AuthForm()
    if auth_form.errors is None:
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'users/login.html', context=context)


def logout_view(request):
    logout(request)
    # return HttpResponse('Вы успешно вышли из своей учетной записи')
    return HttpResponseRedirect(redirect_to='/')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            row_password = form.cleaned_data.get('password1')
            birthday = form.cleaned_data.get('birthday')
            city = form.cleaned_data.get('city')
            user = authenticate(username=username, password=row_password, date_of_birth=birthday, city=city)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@transaction.atomic
def another_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            UserProfile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth
            )
            username = form.cleaned_data.get('username')
            row_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=row_password)
            login(request, user)
            return redirect('main')
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



def replenish_balance_view(request):
    if request.method == 'POST':
        form = UpdateBalanceForm(request.POST)
        if form.is_valid():
            balance = form.cleaned_data.get('balance')
            update_balance(user_id=request.user.id, balance=balance)
            logger.info(f'Пользователь {request.user} пополнил баланс на сумму {balance}')
            return HttpResponseRedirect(reverse('account'))
        pass
    update_balance_form = UpdateBalanceForm()
    context = {
        'form': update_balance_form
    }
    return render(request, 'users/update_balance.html', context=context)