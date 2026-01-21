from django.db import models
from salons.models import Salon
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import jdatetime
from django.core.exceptions import ValidationError
from salons.models import SalonBaseModel


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    age = models.PositiveIntegerField(null=True,blank=True,verbose_name=_('age')) #adad mosbat : sen
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name=_('phone number'))
    salon = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('salon')
    )
    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        elif self.salon:
            return f"{self.username} | {self.salon}"
        else:
            return self.username
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser and not obj.salon:
            raise ValidationError("مدیر سالن باید به یک سالن متصل باشد")
        super().save_model(request, obj, form, change)

MONTH_CHOICES = (
    (1, _('month 1')),
    (2, _('month 2')),
    (3, _('month 3')),
    (4, _('month 4')),
    (5, _('month 5')),
    (6, _('month 6')),
    (7, _('month 7')),
    (8, _('month 8')),
    (9, _('month 9')),
    (10, _('month 10')),
    (11, _('month 11')),
    (12, _('month 12')),
)
class Customer(SalonBaseModel):
    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')
        ordering = ['-created_at']
    first_name = models.CharField(max_length=100 , verbose_name=_('first name'))
    last_name = models.CharField(max_length=100 , verbose_name=_('last name'))
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name=_('phone number'))
    birth_date = models.DateField(null=True, blank=True, verbose_name=_('birth date'))
    birth_month = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        choices=MONTH_CHOICES,
        verbose_name=_('birth month')
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at') )
    is_active = models.BooleanField(default=True , verbose_name=_('active'))
    note = models.TextField(blank=True, verbose_name=_('note'))

    def __str__(self):
        return f"{ self.first_name} {self.last_name} ({self.phone_number})"    

    def save(self, *args, **kwargs):
        if self.birth_date and not self.birth_month:
            j_date = jdatetime.date.fromgregorian(date=self.birth_date)
            self.birth_month = j_date.month
            # self.birth_month = self.birth_date.month
        super().save(*args, **kwargs)