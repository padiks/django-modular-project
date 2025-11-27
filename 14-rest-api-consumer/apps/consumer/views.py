# apps/consumer/views.py
import requests
from django.shortcuts import render

def index(request):
    # Fetch data from the external API
    api_url = "https://padiks.pythonanywhere.com/api/books/"
    response = requests.get(api_url)

    # if not any(group in allowed_groups for group in user_groups):
        # If the user is not in one of the allowed groups, deny access
        # return HttpResponseForbidden("You do not have permission to view this data.")		
	
    if response.status_code == 200:
        # Since the API returns a list of books, we can directly assign the list to books_data
        books_data = response.json()  # No need to use .get() here, as the response is a list
        context = {
            'title': 'Books List',
            'books': books_data,  # Passing the list directly
        }
    else:
        context = {
            'title': 'Books List',
            'books': [],
            'error': 'Failed to fetch data from API'
        }

    return render(request, 'consumer/index.html', context)
	