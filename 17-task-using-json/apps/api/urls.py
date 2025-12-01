# apps/api/urls.py
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

app_name = 'api'  # Add this line to define the namespace

router = DefaultRouter()
router.register(r'books', BookViewSet)  # Register the BookViewSet

urlpatterns = router.urls
