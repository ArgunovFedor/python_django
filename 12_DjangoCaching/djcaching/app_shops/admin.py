from django.contrib import admin
from app_shops.models import Shop


# Register your models here.

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Shop, ShopAdmin)
