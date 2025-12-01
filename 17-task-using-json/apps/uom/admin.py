# apps/uom/admin.py
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import StockItemUOM

class StockItemUOMAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'name', 'description', 'status', 'created_at', 'updated_at')

    search_fields = ['name']
    list_filter = ['status']
    list_display = ['name', 'status', 'created_at', 'updated_at']

    # ---- GROUP BASED PERMISSIONS ----
    def has_view_permission(self, request, obj=None):
        # Admin group OR Superuser → full access
        if request.user.is_superuser:
            return True
        if request.user.groups.filter(name='Admin').exists():
            return True
        
        # Users group can VIEW only
        if request.user.groups.filter(name='Users').exists():
            return True

        return False

    def has_add_permission(self, request):
        # Only Admin group or superuser
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name='Admin').exists()

    def has_change_permission(self, request, obj=None):
        # Only Admin group or superuser
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name='Admin').exists()

    def has_delete_permission(self, request, obj=None):
        # Only Admin group or superuser
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name='Admin').exists()

    def has_module_permission(self, request):
        # Must allow Users + Admins to see the app in Django Admin menu
        if request.user.is_superuser:
            return True
        if request.user.groups.filter(name='Admin').exists():
            return True
        if request.user.groups.filter(name='Users').exists():
            return True
        return False

admin.site.register(StockItemUOM, StockItemUOMAdmin)
