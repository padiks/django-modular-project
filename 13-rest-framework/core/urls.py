# core/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # Import views to access the render_markdown_view function

urlpatterns = [
    path('admin/', admin.site.urls),
	
    path('compute/', include('apps.compute.urls')),  # Samples
	
    path('markdown/', views.render_markdown_view, name='render_markdown'),
    path('markdown/<str:filename>/', views.render_markdown_file, name='render_markdown_file'),  # Handle specific markdown file	
	
    path('', include('apps.movements.urls')),  # Home page (2)
    path('uom/', include('apps.uom.urls')), 
    path('categories/', include('apps.categories.urls')),
    path('doctype/', include('apps.doctype.urls')),
    path('items/', include('apps.items.urls')),
    path('users/', include('apps.users.urls')),
    path('api/', include('apps.api.urls')),  # API base path for the 'api' app	
]


# core/urls.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# from django.conf import settings  # For DEBUG
# Debug Toolbar URLs only if DEBUG=True
# if settings.DEBUG:
#   import debug_toolbar
#    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
