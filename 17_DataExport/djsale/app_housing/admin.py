from django.contrib import admin

from app_housing.models import TypeOfHouse, Housing, QuantityOfRooms


# Register your models here.

class TypeOfHouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class HousingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'type_of_house', 'quantity_of_rooms']


class QuantityOfRoomsAdmin(admin.ModelAdmin):
    list_display = ['id', 'count', 'name']


admin.site.register(TypeOfHouse, TypeOfHouseAdmin)
admin.site.register(Housing, HousingAdmin)
admin.site.register(QuantityOfRooms, QuantityOfRoomsAdmin)
