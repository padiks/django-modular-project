# apps/consumer/urls.py
from django.urls import path
from . import views

app_name = 'consumer'

urlpatterns = [
    path('', views.index, name='index'),
]
