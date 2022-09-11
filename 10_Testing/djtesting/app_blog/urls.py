from django.urls import path
from app_blog.views import BlogListView, BlogUpdateView, BlogDetailView, BlogCreateView

urlpatterns = [
    path('list/', BlogListView.as_view(), name='blog_list'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new/', BlogCreateView.as_view(), name='blog_create'),
  ]