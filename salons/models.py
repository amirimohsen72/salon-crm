from django.db import models
from django.utils.translation import gettext_lazy as _


class Salon(models.Model):
    class Meta:
        verbose_name = _('salon')
        verbose_name_plural = _('salons')

    name = models.CharField(
        max_length=200,
        verbose_name=_('salon name')
    )

    owner_name = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_('owner name')
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_('phone number')
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('active')
    )

    subscription_expire_at = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('subscription expire date')
    )

    # تنظیمات پیامک (فعلاً ساده)
    sms_provider = models.CharField(
        max_length=50,
        default='dummy',
        verbose_name=_('sms provider')
    )

    sms_sender = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('sms sender number')
    )

    sms_api_key = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('sms api key')
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_('city')
    )
    address = models.TextField(
        blank=True,
        verbose_name=_('address')
    )
    support_phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_('support phone')
    )
    slug = models.SlugField(
        unique=True,
        verbose_name=_('slug')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at')
    )

    def __str__(self):
        return self.name
