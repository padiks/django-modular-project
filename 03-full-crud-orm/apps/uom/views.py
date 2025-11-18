# apps/uom/views.py
import sqlite3
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import StockItemUOM
from .forms import StockItemUOMForm

DB_PATH = settings.BASE_DIR / 'db.sqlite3'


def index(request):
    # List all stock* tables for display only
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'stock%'")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()

    # Only records for stock_items_uom remain active
    records = StockItemUOM.objects.all().order_by('id')

    return render(request, 'uom/index.html', {
        'title': 'UOM List',
        'records': records,
        'tables': tables,  # pass tables to template
    })


def add_record(request):
    if request.method == 'POST':
        form = StockItemUOMForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.created_at = timezone.now()
            record.updated_at = timezone.now()
            record.save()
            return redirect('uom:index')
    else:
        form = StockItemUOMForm()

    return render(request, 'uom/form.html', {
        'title': 'Add UOM',
        'form': form,
    })


def update_record(request, pk):
    record = get_object_or_404(StockItemUOM, pk=pk)

    if request.method == 'POST':
        form = StockItemUOMForm(request.POST, instance=record)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.updated_at = timezone.now()
            updated.save()
            return redirect('uom:index')
    else:
        form = StockItemUOMForm(instance=record)

    return render(request, 'uom/form.html', {
        'title': f'Update UOM ID {record.id}',
        'form': form,
    })


def delete_record(request, pk):
    record = get_object_or_404(StockItemUOM, pk=pk)
    record.delete()
    return redirect('uom:index')
