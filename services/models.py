from django.db import models

from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

    name = models.CharField(max_length=200, verbose_name=_('service name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    price = models.PositiveIntegerField(null=True,blank=True,verbose_name=_('price')) #adad mosbat : toman
    duration= models.PositiveIntegerField(verbose_name=_('duration time'),help_text=_('minute') )
    active = models.BooleanField(default=True, verbose_name=_('active'), )
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('modify date'))

    def __str__(self):
        return self.name