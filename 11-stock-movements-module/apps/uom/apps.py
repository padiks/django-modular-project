# apps/uom/apps.py
from django.apps import AppConfig

# Must match with `core/settings.py`
class UomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.uom'
