# core/urls.py
from django.contrib import admin
from django.urls import path, include
# from django.conf import settings  # For DEBUG

urlpatterns = [
    path('uom/', include('apps.uom.urls')),  # UOM page
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('categories/', include('apps.categories.urls')),
    path('doctype/', include('apps.doctype.urls')),
    path('items/', include('apps.items.urls')),
    path('compute/', include('apps.compute.urls')),
    path('movements/', include('apps.movements.urls')),        
    path('', include('apps.movements.urls')),  # home page
]

# Debug Toolbar URLs only if DEBUG=True
# if settings.DEBUG:
#   import debug_toolbar
#    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
