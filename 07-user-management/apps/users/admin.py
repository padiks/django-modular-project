# apps/users/admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin   # <-- Allow all users to change password

class CustomUserAdmin(UserAdmin):
    # Display key fields to distinguish admins vs users
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')


# Unregister default User admin
admin.site.unregister(User)

# Register custom admin that still includes password change + profile
admin.site.register(User, CustomUserAdmin)
