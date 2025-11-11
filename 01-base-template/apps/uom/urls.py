from django.urls import path
from . import views

app_name = 'home'   # 👈 add this line

urlpatterns = [
    path('', views.index, name='index'),
]
