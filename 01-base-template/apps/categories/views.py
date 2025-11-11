from django.shortcuts import render

# Create a view for categories
def index(request):
    return render(request, 'categories/index.html')  # Ensure this template exists and is valid
