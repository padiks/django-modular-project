# **Guide 2 Step 6: Hook app URLs to project**
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # <-- temporary root redirects to /summation/ for Guide 2
from django.conf import settings  # <-- Import settings for Debug Toolbar condition

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summation/', include('apps.summation.urls')),
    path('', lambda request: redirect('summation/')),  # <-- temporary root redirects to /summation/ for Guide 2
]

# **Guide 4 Step 5: Include the debug toolbar URLs only if DEBUG is True**
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
