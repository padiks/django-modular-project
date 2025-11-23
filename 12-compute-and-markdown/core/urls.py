# core/urls.py
from django.contrib import admin
from django.urls import path, include
# from django.conf import settings  # For DEBUG
from . import views  # Import views to access the render_markdown_view function

urlpatterns = [
    path('admin/', admin.site.urls),
	
    path('compute/', include('apps.compute.urls')),  # Samples
	
    path('markdown/', views.render_markdown_view, name='render_markdown'),
    path('markdown/<str:filename>/', views.render_markdown_file, name='render_markdown_file'),  # Handle specific markdown file	
	
    path('', include('apps.movements.urls')),  # Home page
    path('uom/', include('apps.uom.urls')), 
    path('categories/', include('apps.categories.urls')),
    path('doctype/', include('apps.doctype.urls')),
    path('items/', include('apps.items.urls')),
    path('users/', include('apps.users.urls')),
]

# Debug Toolbar URLs only if DEBUG=True
# if settings.DEBUG:
#   import debug_toolbar
#    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
