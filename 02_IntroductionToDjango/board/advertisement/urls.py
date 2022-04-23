from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='advertisement_list'),
    path('course-<int:num>/', views.course, name='advertisement_list'),
]