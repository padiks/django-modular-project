# apps/movements/apps.py (3)
from django.apps import AppConfig

# Must match with `core/settings.py`
class MovementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.movements'
