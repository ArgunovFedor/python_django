from django.urls import path

from app_users.views import restore_password, login_view, logout_view, register_view, another_register_view, \
    user_account, update_user_account

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('another_register/', another_register_view, name='register'),
    path('account/', user_account, name='account'),
    path('edit_account/', update_user_account, name='edit_account'),
    path('restore_password/', restore_password, name='restore_password')
]
