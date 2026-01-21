from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SalonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'salons'
    verbose_name = _('salons')
