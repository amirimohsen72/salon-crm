from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import timedelta

from accounts.models import Customer
from services.models import Service

class Status(models.TextChoices):
        RESERVED = 'reserved', _('Reserved')
        DONE = 'done', _('Done')
        CANCELED = 'canceled', _('Canceled')

class Appointment(models.Model):
    class Meta:
        verbose_name = _('appointment')
        verbose_name_plural = _('appointments')

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name=_('customer') )
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('created at'))
    reservation_date = models.DateField(
        null=True,
        verbose_name=_('reservation date'),
        db_index=True
    )
    note = models.TextField(
        blank=True,
        verbose_name=_('note')
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.RESERVED,
        verbose_name=_('status')
    )

    def __str__(self):
        return f"{self.customer} ({self.reservation_date})"
    

class AppointmentService(models.Model):
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name='services',
        verbose_name=_('appointment')
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        verbose_name=_('service')
    )
    start_time = models.DateTimeField(verbose_name=_('start time'))
    end_time = models.DateTimeField(blank=True, null=True, verbose_name=_('end time'))

    def save(self, *args, **kwargs):
        if self.start_time:
            self.end_time = self.start_time + timedelta(
                minutes=self.service.duration
            )
        super().save(*args, **kwargs)
