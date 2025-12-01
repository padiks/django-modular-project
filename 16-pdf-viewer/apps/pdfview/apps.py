# apps/pdfview/apps.py
from django.apps import AppConfig

# Must match with `core/settings.py`
class PdfviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.pdfview'
