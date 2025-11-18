# apps/uom/admin.py
from django.contrib import admin
from .models import StockItemUOM

class StockItemUOMAdmin(admin.ModelAdmin):
    # Make all fields read-only
    readonly_fields = ('id', 'name', 'description', 'status', 'created_at', 'updated_at')
    
    # Optionally, you can exclude certain fields from the admin form
    # exclude = ('field_to_exclude',)

    # If you want to make the model non-editable, you can define:
    # fields = ('name', 'description', 'status')  # and exclude other fields from admin
    
    # You can add more filters, ordering, or search fields here if needed
    search_fields = ['name']
    list_filter = ['status']
    list_display = ['name', 'status', 'created_at', 'updated_at']

admin.site.register(StockItemUOM, StockItemUOMAdmin)
