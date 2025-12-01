# apps/modular/urls.py
from django.urls import path
from . import views

app_name = 'modular'

urlpatterns = [
    path('', views.index, name='index'),
]
