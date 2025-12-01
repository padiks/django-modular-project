# apps/categories/admin.py
from django.contrib import admin
from .models import StockItemCategories

class StockItemCategoriesAdmin(admin.ModelAdmin):
    # System fields always read-only
    readonly_fields = ('id', 'created_at', 'updated_at')

    # Search, filter, list display
    search_fields = ['name']
    list_filter = ['status']
    list_display = ['name', 'status', 'created_at', 'updated_at']
    ordering = ['name']

    # Permissions based on group
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Admin').exists():
            return self.readonly_fields  # Admin sees only system read-only fields
        # Users group → everything read-only (won't see table anyway)
        return ('id', 'name', 'description', 'status', 'created_at', 'updated_at')

    def has_add_permission(self, request):
        return request.user.groups.filter(name='Admin').exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()

    def has_view_permission(self, request, obj=None):
        # Only Admins can view this table
        return request.user.groups.filter(name='Admin').exists()


# Register the model
admin.site.register(StockItemCategories, StockItemCategoriesAdmin)
