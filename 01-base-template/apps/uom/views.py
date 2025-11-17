from django.shortcuts import render

# Home page view
def index(request):
    context = {
        'title': 'UOM Home',  # Example context variable
        'welcome_message': 'Welcome to the UOM App!',
    }
    return render(request, 'uom/index.html', context)
