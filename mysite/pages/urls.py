from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('add/', views.add_task_view, name='add_task'),
    path('toggle/<int:task_id>/', views.toggle_task_view, name='toggle_task'),
    path('delete/<int:task_id>/', views.delete_task_view, name='delete_task'),
]
