from django.db import models
from django.utils.translation import gettext_lazy as _

from salons.models import SalonBaseModel

class SMSTemplate(SalonBaseModel):

    class Type(models.TextChoices):
        APPOINTMENT_CONFIRM = 'appointment_confirm', _('appointment confirm')
        APPOINTMENT_REMINDER = 'appointment_reminder', _('appointment reminder')
        BIRTHDAY = 'birthday', _('birthday')
        PROMOTION = 'promotion', _('promotion')
        CUSTOM = 'custom', _('custom')
    class Meta:
        verbose_name = _('sms template')
        verbose_name_plural = _('sms templates')

    title = models.CharField(max_length=100, verbose_name=_('title'))
    message = models.TextField(verbose_name=_('formated message'),help_text=_('can use variables like {{name}}, {{date}}, {{time}}'))
    type = models.CharField(max_length=30, choices=Type.choices, verbose_name=_('template type'))
    is_active = models.BooleanField(default=True, verbose_name=_('active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('modified at'))

    def __str__(self):
        return self.title

class SMSLog(SalonBaseModel):
    class Status(models.TextChoices):
        PENDING = 'pending', _('pending')
        SENT = 'sent', _('sent')
        FAILED = 'failed', _('failed')
    class Meta:
        verbose_name = _('sms log')
        verbose_name_plural = _('sms logs')
    template = models.ForeignKey(
        'notifications.SMSTemplate',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('template')
    )

    customer = models.ForeignKey(
        'accounts.Customer',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('customer')
    )

    appointment = models.ForeignKey(
        'appointments.Appointment',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('appointment')
    )

    phone_number = models.CharField(
        max_length=15,
        verbose_name=_('phone number')
    )

    message = models.TextField(
        verbose_name=_('final message')
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name=_('status')
    )

    provider_response = models.TextField(
        blank=True,
        verbose_name=_('provider response')
    )

    sent_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('sent at')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at')
    )

    def __str__(self):
        return f"{self.phone_number} - {self.status}"
