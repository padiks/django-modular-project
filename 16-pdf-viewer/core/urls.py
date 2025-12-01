# core/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views                         # Import views to access the render_markdown_view function
from apps.users import views as user_views  # Root URL is login page
from django.conf import settings            # PDFview 
from django.conf.urls.static import static   


urlpatterns = [
    path('admin/', admin.site.urls),
	
    path('markdown/', views.render_markdown_view, name='render_markdown'),
    path('markdown/<str:filename>/', views.render_markdown_file, name='render_markdown_file'),  # Handle specific markdown file	
	
    # Root URL is login page
    path('', user_views.login_view, name='login'),  
    path('logout/', user_views.logout_view, name='logout'),

    # Movements section (post-login landing page)
    path('movements/', include('apps.movements.urls')),

    path('uom/', include('apps.uom.urls')), 
    path('categories/', include('apps.categories.urls')),
    path('doctype/', include('apps.doctype.urls')),
    path('items/', include('apps.items.urls')),
    path('users/', include('apps.users.urls')),

    path('modular/', include('apps.modular.urls')),
    path('compute/', include('apps.compute.urls')),
    path('excel/', include('apps.excel.urls')),
    path('pdfview/', include('apps.pdfview.urls')),  # PDFview

    path('api/', include('apps.api.urls')),  # API base path for the 'api' app	
    path('consumer/', include('apps.consumer.urls')),  # Consumer path for Rest API Framework
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # PDFview


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
