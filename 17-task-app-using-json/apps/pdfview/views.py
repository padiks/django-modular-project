# apps/pdfview/views.py
from django.shortcuts import render


def index(request):
    return render(request, 'pdfview/index.html', {
        'title': 'PDF Viewer',
        'pdf_url': '/media/README.pdf',   # tell template where PDF is
    })
