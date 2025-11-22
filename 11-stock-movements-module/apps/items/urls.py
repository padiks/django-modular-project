# apps/items/urls.py
from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_record, name='add_record'),  # This must match the URL used in the template
    path('update/<int:pk>/', views.update_record, name='update_record'),
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),
]
