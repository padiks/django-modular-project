# apps/users/admin.py
from django.contrib import admin
from django.contrib.auth.models import User

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_active')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

