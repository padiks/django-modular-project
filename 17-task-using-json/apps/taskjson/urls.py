# apps/taskjson/urls.py
from django.urls import path
from . import views

app_name = 'taskjson'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
