from django.contrib import admin
from django import forms
from .models import Service
from jalali_date.admin import ModelAdminJalaliMixin



@admin.register(Service)
class ServiceAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'active','datetime_modified')
    list_filter = ('active',)
    search_fields = ('name', )
    widgets = {
        'duration':forms.DurationField,
    }
