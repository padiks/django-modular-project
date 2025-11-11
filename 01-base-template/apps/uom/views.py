from django.shortcuts import render
from django.http import HttpResponse

# The index view
def index(request):
    return render(request, 'uom/index.html')  # Ensure this template exists and is valid

# Simple view for testing
# def simple_view(request):
#    return HttpResponse("Hello, World!")
	
		