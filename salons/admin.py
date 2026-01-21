from django.contrib import admin
from .models import Salon
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(Salon)
class SalonAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = (
        'name',
        'owner_name',
        'phone_number',
        'is_active',
        'subscription_expire_at',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
        'owner_name',
        'phone_number',
    )

    readonly_fields = (
        'created_at',
    )
