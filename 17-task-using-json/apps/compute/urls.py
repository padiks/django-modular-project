# apps/compute/urls.py
from django.urls import path
from . import views

app_name = 'compute'  # Add this line to set the namespace

urlpatterns = [
    path('summation/', views.summation, name='summation'),  # Route for summation
    path('summary/', views.summary, name='summary'),        # Route for summary
]
