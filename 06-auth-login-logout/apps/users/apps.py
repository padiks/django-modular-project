# apps/users/apps.py - 3
# core/settings.py - 2
# core/urls.py - 1
# Must match with `core/settings.py`
from django.apps import AppConfig

class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
