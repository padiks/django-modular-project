# apps/uom/views.py
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import sqlite3
from .models import StockItemUOM
from .forms import StockItemUOMForm

DB_PATH = settings.BASE_DIR / 'db.sqlite3'


@login_required
def index(request):
    # Get logged-in user's primary group
    user_groups = request.user.groups.values_list('name', flat=True)
    user_group = user_groups[0] if user_groups else None

    # List all stock* tables for display only
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'stock%'")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()

    # Only records for stock_items_uom
    records = StockItemUOM.objects.all().order_by('id')

    return render(request, 'uom/index.html', {
        'title': 'Stock Items UOM List',
        'records': records,
        'tables': tables,
        'current_table': 'stock_items_uom',
        'user_group': user_group,
    })


@login_required
def add_record(request):
    # Users group cannot add
    if not (request.user.is_superuser or request.user.groups.filter(name='Admin').exists()):
        messages.warning(request, "You do not have permission to add UOM records.")
        return redirect('uom:index')

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


@login_required
def update_record(request, pk):
    record = get_object_or_404(StockItemUOM, pk=pk)

    # Users group cannot edit
    if not (request.user.is_superuser or request.user.groups.filter(name='Admin').exists()):
        messages.warning(request, "You do not have permission to edit UOM records.")
        return redirect('uom:index')

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


@login_required
def delete_record(request, pk):
    record = get_object_or_404(StockItemUOM, pk=pk)

    # Users group cannot delete
    if not (request.user.is_superuser or request.user.groups.filter(name='Admin').exists()):
        messages.warning(request, "You do not have permission to delete UOM records.")
        return redirect('uom:index')

    record.delete()
    return redirect('uom:index')
