# apps/users/admin.py
from django.contrib import admin
from django.contrib.auth.models import User

class CustomUserAdmin(admin.ModelAdmin):
    # Display key fields to easily distinguish admins vs normal users
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')

# Unregister default User admin
admin.site.unregister(User)
# Register custom admin
admin.site.register(User, CustomUserAdmin)
