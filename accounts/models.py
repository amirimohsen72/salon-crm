from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    age = models.PositiveIntegerField(null=True,blank=True,verbose_name=_('age')) #adad mosbat : sen
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name=_('phone number'))

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.username



class Customer(models.Model):
    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')
        ordering = ['-created_at']
    first_name = models.CharField(max_length=100 , verbose_name=_('first name'))
    last_name = models.CharField(max_length=100 , verbose_name=_('last name'))
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name=_('phone number'))
    birth_date = models.DateField(null=True, blank=True, verbose_name=_('birth date'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at') )
    is_active = models.BooleanField(default=True , verbose_name=_('active'))
    note = models.TextField(blank=True, verbose_name=_('note'))

    def __str__(self):
        return f"{ self.first_name} {self.last_name} ({self.phone_number})"    

