# apps/items/admin.py
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import StockItems

class StockItemsAdmin(admin.ModelAdmin):

    # System fields always read-only
    readonly_fields = ('id', 'created_at', 'updated_at')

    search_fields = ['code', 'description']
    list_filter = ['status', 'category', 'uom']
    list_display = ['code', 'description', 'category', 'uom', 'status', 'created_at', 'updated_at']
    ordering = ['code']

    # Admin group → full access
    # Users group → no access (model hidden), but we still define checks for safety
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Admin').exists():
            return self.readonly_fields  # admin sees only system read-only fields
        return (
            'id', 'code', 'description', 'category', 'uom',
            'status', 'created_at', 'updated_at'
        )

    def has_add_permission(self, request):
        return request.user.groups.filter(name='Admin').exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()

    def has_view_permission(self, request, obj=None):
        # Only Admins can VIEW this table
        return request.user.groups.filter(name='Admin').exists()


admin.site.register(StockItems, StockItemsAdmin)
