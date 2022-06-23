from django.contrib import admin
from app_library.models import Waiter,  Restaurant


class TestInline(admin.TabularInline):
    model = Waiter

@admin.register(Waiter)
class WaiterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city']
    list_filter = ['first_name']

    fieldsets = (
        ('Основные сведения', {
            'fields': ('first_name', 'last_name', 'country', 'city')
        }),
        ('Биографические данные', {
            'fields': ('university', 'birth_date', 'biography'),
            'description': 'Различные данные из биографии автора',
            'classes': ['collapse']
        }),
        ('Контакты', {
            'fields': ('email', 'phone', 'personal_page', 'facebook', 'twitter'),
            'description': 'Различные способы связаться с автором'
        })
    )

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rating']
    search_fields = ['name', 'rating']
    inlines = [TestInline]