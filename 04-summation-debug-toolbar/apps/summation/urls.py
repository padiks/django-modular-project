# apps/summation/urls.py
# **Guide 2 Step 5: Create app-specific URLs**

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='summation_index'),
]
