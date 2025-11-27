# apps/doctype/apps.py
from django.apps import AppConfig

# Must match with `core/settings.py`
class DocTypeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.doctype'
