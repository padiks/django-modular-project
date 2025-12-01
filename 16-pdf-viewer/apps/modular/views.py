# apps/modular/views.py
from django.shortcuts import render


def index(request):

    return render(request, 'modular/index.html', {
        'title': 'Modular Template',
    })
