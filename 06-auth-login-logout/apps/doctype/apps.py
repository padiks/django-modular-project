# apps/<app-name>/apps.py - 3
from django.apps import AppConfig

class DocTypeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.doctype' # <-- must match with `core/settings.py`
