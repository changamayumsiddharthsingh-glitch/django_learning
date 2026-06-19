from django.contrib import admin
from .models import Task, Page, GalleryImage

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Task)
admin.site.register(GalleryImage)


