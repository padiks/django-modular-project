# apps/<app-name>/urls.py
from django.urls import path
from . import views

app_name = 'compute'

urlpatterns = [
    path('', views.index, name='index'),
]
