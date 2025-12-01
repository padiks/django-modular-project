# apps/pdfview/urls.py
from django.urls import path
from . import views

app_name = 'pdfview'

urlpatterns = [
    path('', views.index, name='index'),
]
