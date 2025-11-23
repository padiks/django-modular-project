# apps/users/admin.py
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):

    # Display key fields
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')

    # Admin group → full access
    # Users group → no access (model hidden)
    def has_view_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists() or request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists() or request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.groups.filter(name='Admin').exists() or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists() or request.user.is_superuser

# Unregister default User admin
admin.site.unregister(User)

# Register custom User admin
admin.site.register(User, CustomUserAdmin)
