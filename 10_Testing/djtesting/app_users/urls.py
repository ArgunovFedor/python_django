from django.urls import path

from app_users.views import login_view, account_view, another_register_view, register_view, logout_view, \
    edit_account_view, restore_password

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('another_register/', another_register_view, name='register'),
    path('account/', account_view, name='account'),
    path('edit_account/', edit_account_view, name='edit_account'),
    path('restore_password/', restore_password, name='restore_password')
]