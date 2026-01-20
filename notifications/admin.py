from django.contrib import admin
from .models import SMSTemplate, SMSLog
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(SMSTemplate)
class SMSTemplateAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'is_active', 'updated_at')
    list_filter = ('type', 'is_active')
    search_fields = ('title', 'message')
    ordering = ('-updated_at',)


@admin.register(SMSLog)
class SMSLogAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'customer', 'appointment', 'status', 'sent_at', 'created_at')
    list_filter = ('status', 'template', 'created_at')
    search_fields = ('phone_number', 'message', 'customer__first_name', 'customer__last_name')
    readonly_fields = ('created_at', 'sent_at', 'provider_response')
    ordering = ('-created_at',)
