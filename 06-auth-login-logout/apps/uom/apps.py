# apps/uom/apps.py
from django.apps import AppConfig

class UomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.uom' # <-- must match with `core/settings.py`
