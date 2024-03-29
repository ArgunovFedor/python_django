"""djsale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from app_news.sitemap import NewsSitemap, HousingSitemap
from djsale.views import MainView, AboutUs, Contacts

sitemaps = {
    'news': NewsSitemap,
    'housing': HousingSitemap
}

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('about_us/', AboutUs.as_view(), name='about_us'),
    path('contacts', Contacts.as_view(), name='contacts'),
    path('admin/', admin.site.urls),
    path('news/', include('app_news.urls')),
    path('housing/', include('app_housing.urls')),
    path('rss/', include('app_rss.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]
