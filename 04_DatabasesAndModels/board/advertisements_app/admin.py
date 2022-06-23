from django.contrib import admin
from advertisements_app.models import Advertisement, Author, AdvertisementType, News, Comments


class CommentInline(admin.TabularInline):
    model = Comments


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(AdvertisementType)
class AdvertisementTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_filter = ['is_active']
    list_display = ['id', 'name', 'created_at', 'is_active']
    inlines = [CommentInline]
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_as_inactive(self, request, queryset):
        queryset.update(is_active=False)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'text']
    list_filter = ['username']
    actions = ['change_text_to_delete']


    def change_text_to_delete(self,request,queryset):
        queryset.update(text='Удалено администратором')

    change_text_to_delete.short_description = 'Изменить текст на удалено администратором'