# apps/<app-name>/views.py
import sqlite3
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import StockItemCategories
from .forms import StockItemCategoriesForm

DB_PATH = settings.BASE_DIR / 'db.sqlite3'

def index(request):
    # List all stock* tables for display only
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'stock%'")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()

    records = StockItemCategories.objects.all().order_by('id')

    return render(request, 'categories/index.html', {
        'title': 'Categories List - Database db.sqlite3 / SQLite Tables',
        'records': records,
        'tables': tables,
        'current_table': 'stock_items_categories',
    })

def add_record(request):
    if request.method == 'POST':
        form = StockItemCategoriesForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            now = timezone.now()
            record.created_at = now
            record.updated_at = now
            record.save()
            return redirect('categories:index')
    else:
        form = StockItemCategoriesForm()

    return render(request, 'categories/form.html', {
        'title': 'Add Category',
        'form': form,
    })


def update_record(request, pk):
    record = get_object_or_404(StockItemCategories, pk=pk)

    if request.method == 'POST':
        form = StockItemCategoriesForm(request.POST, instance=record)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.updated_at = timezone.now()
            updated.save()
            return redirect('categories:index')
    else:
        form = StockItemCategoriesForm(instance=record)

    return render(request, 'categories/form.html', {
        'title': f'Update Category ID {record.id}',
        'form': form,
    })


def delete_record(request, pk):
    record = get_object_or_404(StockItemCategories, pk=pk)
    record.delete()
    return redirect('categories:index')
