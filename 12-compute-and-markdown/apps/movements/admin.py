# apps/movements/admin.py (6) (c)
from django.contrib import admin
from .models import StockMovements

class StockMovementsAdmin(admin.ModelAdmin):

    # System fields always read-only
    readonly_fields = ('id', 'created_at', 'updated_at')

    list_display = [
        'id',
        'item',
        'document_type',
        'document_number',
        'quantity',
        'status',
        'movement_date',
        'created_at',
        'updated_at',
    ]

    search_fields = [
        'document_reference',
        'document_number',
        'item__code',
        'document_type__name',
    ]

    list_filter = [
        'status',
        'document_type',
        'item',
    ]

    ordering = ['-movement_date']

    # Permission rules
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Admin').exists():
            return self.readonly_fields
        return (
            'id', 'item', 'document_type', 'document_number', 'document_reference',
            'quantity', 'status', 'movement_date', 'created_at', 'updated_at'
        )

    def has_add_permission(self, request):
        return request.user.groups.filter(name='Admin').exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()

    def has_view_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()


admin.site.register(StockMovements, StockMovementsAdmin)

