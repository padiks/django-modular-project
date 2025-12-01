# apps/movements/views.py (6)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import sqlite3

from .models import StockMovements
from .forms import StockMovementsForm

DB_PATH = settings.BASE_DIR / 'db.sqlite3'


@login_required
def index(request):
    # Get logged-in user's primary group
    user_groups = request.user.groups.values_list('name', flat=True)
    user_group = user_groups[0] if user_groups else None

    # List all stock* tables (display only)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'stock%'")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()

    # Fetch all StockMovements
    records = StockMovements.objects.all().order_by('-id')

    return render(request, 'movements/index.html', {
        'title': 'Stock Movements List',
        'records': records,
        'tables': tables,
        'current_table': 'stock_movements',
        'user_group': user_group,
    })


@login_required
def add_record(request):
    # Users group cannot add
    if not (request.user.is_superuser or request.user.groups.filter(name='Admin').exists()):
        messages.warning(request, "You do not have permission to add stock movements.")
        return redirect('movements:index')

    if request.method == 'POST':
        form = StockMovementsForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            now = timezone.now()
            record.created_at = now
            record.updated_at = now
            record.save()
            return redirect('movements:index')
    else:
        form = StockMovementsForm()

    return render(request, 'movements/form.html', {
        'title': 'Add Stock Movement',
        'form': form,
    })


@login_required
def update_record(request, pk):
    record = get_object_or_404(StockMovements, pk=pk)

    # Users group cannot edit
    if not (request.user.is_superuser or request.user.groups.filter(name='Admin').exists()):
        messages.warning(request, "You do not have permission to edit stock movements.")
        return redirect('movements:index')

    if request.method == 'POST':
        form = StockMovementsForm(request.POST, instance=record)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.updated_at = timezone.now()
            updated.save()
            return redirect('movements:index')
    else:
        form = StockMovementsForm(instance=record)

    return render(request, 'movements/form.html', {
        'title': f'Update Movement ID {record.id}',
        'form': form,
    })


@login_required
def delete_record(request, pk):
    record = get_object_or_404(StockMovements, pk=pk)

    # Users group cannot delete
    if not (request.user.is_superuser or request.user.groups.filter(name='Admin').exists()):
        messages.warning(request, "You do not have permission to delete stock movements.")
        return redirect('movements:index')

    record.delete()
    return redirect('movements:index')
