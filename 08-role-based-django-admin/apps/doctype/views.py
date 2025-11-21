# apps/doctype/views.py
from django.contrib.auth.decorators import login_required
import sqlite3
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import StockDocType
from .forms import StockDocTypeForm

DB_PATH = settings.BASE_DIR / 'db.sqlite3'


@login_required
def index(request):
    # --- Get logged-in user's primary group ---
    user_groups = request.user.groups.values_list('name', flat=True)
    user_group = user_groups[0] if user_groups else None

    # --- List all stock* tables for display only ---
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'stock%'")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()

    # --- Fetch all StockDocType records ---
    records = StockDocType.objects.all().order_by('id')

    return render(request, 'doctype/index.html', {
        'title': 'Stock Document Type List',
        'records': records,
        'tables': tables,
        'current_table': 'stock_document_type',
        'user_group': user_group,  # pass group to template
    })


@login_required
def add_record(request):
    if request.method == 'POST':
        form = StockDocTypeForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            now = timezone.now()
            record.created_at = now
            record.updated_at = now
            record.save()
            return redirect('doctype:index')
    else:
        form = StockDocTypeForm()

    return render(request, 'doctype/form.html', {
        'title': 'Add Document Type',
        'form': form,
    })


@login_required
def update_record(request, pk):
    record = get_object_or_404(StockDocType, pk=pk)

    if request.method == 'POST':
        form = StockDocTypeForm(request.POST, instance=record)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.updated_at = timezone.now()
            updated.save()
            return redirect('doctype:index')
    else:
        form = StockDocTypeForm(instance=record)

    return render(request, 'doctype/form.html', {
        'title': f'Update Document Type ID {record.id}',
        'form': form,
    })


@login_required
def delete_record(request, pk):
    record = get_object_or_404(StockDocType, pk=pk)
    record.delete()
    return redirect('doctype:index')

