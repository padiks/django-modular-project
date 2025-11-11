from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('uom/', include('apps.uom.urls')),
    path('categories/', include('apps.categories.urls')),
    path('', include('apps.uom.urls')),  # 👈 add this line
]
