from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from app_users.models import UserProfile


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=100, required=False, help_text='Фамилия')
    email = forms.EmailField()
    date_of_birth = forms.DateField(required=True, help_text='Дата рождения')
    city = forms.CharField(required=False, help_text='Город', max_length=36)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class RestorePasswordForm(forms.Form):
    email = forms.EmailField()


class EditAccountForm(forms.ModelForm):
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('date_of_birth', 'city')


class UpdateBalanceForm(forms.Form):
    balance = forms.IntegerField(required=True)