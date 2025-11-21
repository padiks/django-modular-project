# apps/items/views.py
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import sqlite3
from .models import StockItems
from .forms import StockItemsForm

DB_PATH = settings.BASE_DIR / 'db.sqlite3'

@login_required
def index(request):
    # Get logged-in user's primary group (Admin / Users)
    user_groups = request.user.groups.values_list('name', flat=True)
    user_group = user_groups[0] if user_groups else None

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
        'user_group': user_group,  # pass group to template
    })


@login_required
def add_record(request):
    if request.method == 'POST':
        form = StockItemsForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.created_at = timezone.now()
            record.updated_at = timezone.now()
            record.save()
            return redirect('items:index')
    else:
        form = StockItemsForm()

    return render(request, 'items/form.html', {
        'title': 'Add Stock Item',
        'form': form,
    })


@login_required
def update_record(request, pk):
    record = get_object_or_404(StockItems, pk=pk)

    if request.method == 'POST':
        form = StockItemsForm(request.POST, instance=record)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.updated_at = timezone.now()
            updated.save()
            return redirect('items:index')
    else:
        form = StockItemsForm(instance=record)

    return render(request, 'items/form.html', {
        'title': f'Update Stock Item ID {record.id}',
        'form': form,
    })


@login_required
def delete_record(request, pk):
    record = get_object_or_404(StockItems, pk=pk)
    record.delete()
    return redirect('items:index')
