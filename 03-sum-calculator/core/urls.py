# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Add this for redirection

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/sum/')),  # Redirect root URL to /sum/
    path('sum/', include('sum.urls')),  # Include sum app URLs
]
