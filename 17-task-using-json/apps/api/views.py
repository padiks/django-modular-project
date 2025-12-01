# apps/api/views.py
from rest_framework import viewsets
# from rest_framework.permissions import IsAdminUser
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow only GET requests
    http_method_names = ['get']

    # Only admin can modify data
    # permission_classes = [IsAdminUser]