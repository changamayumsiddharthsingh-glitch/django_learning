from django.contrib import admin
from .models import Category, Post, Page, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'status', 'published_at', 'created_at')
    list_filter = ('status', 'created_at', 'category')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    date_hierarchy = 'published_at'
    ordering = ('-published_at', '-created_at')

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author_name', 'content')
