from django.contrib import admin
from .models import Appointment, AppointmentService


class AppointmentServiceInline(admin.TabularInline):
    model = AppointmentService
    extra = 1
    autocomplete_fields = ['service']
    fields = ('service', 'start_time', 'end_time')
    readonly_fields = ('end_time',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('customer__first_name', 'customer__last_name', 'customer__phone_number')
    inlines = [AppointmentServiceInline]
