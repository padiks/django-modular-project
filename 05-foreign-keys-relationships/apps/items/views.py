# apps/items/views.py - 4
import sqlite3
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import StockItems  # Import the StockItems model
from .forms import StockItemsForm  # Import the StockItems form

DB_PATH = settings.BASE_DIR / 'db.sqlite3'

def index(request):
    # List all stock* tables for display only
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'stock%'")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()

    # Fetch all StockItems
    records = StockItems.objects.all().order_by('id')

    return render(request, 'items/index.html', {
        'title': 'Stock Items List',
        'records': records,
        'tables': tables,
        'current_table': 'stock_items',
    })

def add_record(request):
    if request.method == 'POST':
        form = StockItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items:index')  # Redirect to the list of items after saving
    else:
        form = StockItemsForm()
    return render(request, 'items/form.html', {'title': 'Add Stock Item', 'form': form})

def update_record(request, pk):
    record = get_object_or_404(StockItems, pk=pk)
    if request.method == 'POST':
        form = StockItemsForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('items:index')  # Redirect to the list of items after updating
    else:
        form = StockItemsForm(instance=record)
    return render(request, 'items/form.html', {'title': 'Update Stock Item', 'form': form})

def delete_record(request, pk):
    record = get_object_or_404(StockItems, pk=pk)
    record.delete()
    return redirect('items:index')  # Redirect to the list of items after deleting
