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

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.RESERVED
    )

    def __str__(self):
        return f"{self.customer} ({self.id})"
    

class AppointmentService(models.Model):
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name='services'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.start_time:
            self.end_time = self.start_time + timedelta(
                minutes=self.service.duration
            )
        super().save(*args, **kwargs)
