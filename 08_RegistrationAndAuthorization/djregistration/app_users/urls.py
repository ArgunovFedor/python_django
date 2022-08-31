from django.urls import path

from app_users import views
from app_users.views import login_view, account_view, another_register_view, register_view, logout_view, \
    AnotherLoginView, AnotherLogoutView

urlpatterns = [
    path('', views.advertisement_list, name='categories_list'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('another_login', AnotherLoginView.as_view(), name='another_login'),
    path('advertisements', views.AdvertisementListView.as_view(), name='advertisements'),
    path('advertisements/<int:pk>', views.AdvertisementDetailView.as_view(), name='advertisements-detail'),
    path('news', views.NewsListView.as_view(), name='news'),
    path('news/<int:pk>', views.NewsListDetailView.as_view(), name='news-detail'),
    path('news/update/<int:pk>', views.NewsUpdateView.as_view(), name='news-update'),
    path('news/new/', views.NewsCreateView.as_view(), name='news-create'),
    path('comments/new/<int:pk>', views.CommentsCreateView.as_view(), name='comments-create'),
    path('comments', views.CommentsListView.as_view(), name='comments'),
    path('comments/<int:pk>', views.CommentsListDetailView.as_view(), name='comments-detail'),
    path('register/', register_view, name='register'),
    path('another_register/', another_register_view, name='register'),
    path('account/', account_view, name='account')
]