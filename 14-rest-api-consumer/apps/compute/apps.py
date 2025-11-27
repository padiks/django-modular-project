# apps/<app-name>/apps.py
from django.apps import AppConfig

# must match with `core/settings.py`
class ComputeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.compute' 
