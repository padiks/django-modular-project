# apps/items/apps.py - 1
from django.apps import AppConfig

class ItemsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.items'  # <-- must match with `core/settings.py`
