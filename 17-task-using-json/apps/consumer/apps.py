# apps/consumer/apps.py
from django.apps import AppConfig

# Must match with `core/settings.py`
class ConsumerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.consumer'
