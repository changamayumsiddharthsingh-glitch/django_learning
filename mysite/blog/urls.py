from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('post/<slug:slug>/', views.post_detail_view, name='post_detail'),
    path('category/<slug:slug>/', views.category_posts_view, name='category_posts'),
    path('page/<slug:slug>/', views.page_detail_view, name='page_detail'),
]
