# Guide 1
# from django.shortcuts import render
# Home page view
# def index(request):
#    context = {
#        'title': 'UOM Home',  # Example context variable
#        'welcome_message': 'Welcome to the UOM App!',
#    }
#    return render(request, 'uom/index.html', context)
from django.shortcuts import render
from .models import StockItemUOM

def index(request):
    records = StockItemUOM.objects.all()  # ORM reading existing rows

    return render(request, 'uom/index.html', {
        'title': 'UOM Home',
        'welcome_message': 'Dumping Data via Django ORM',
        'records': records,
    })
