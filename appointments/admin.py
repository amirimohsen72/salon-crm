from django.contrib import admin
from .models import Appointment, AppointmentService
from jalali_date.admin import ModelAdminJalaliMixin
from django.utils.translation import gettext as _
from django.utils.timezone import localtime
from jalali_date import jdatetime


class AppointmentServiceInline(ModelAdminJalaliMixin,admin.TabularInline):
    model = AppointmentService
    extra = 1
    autocomplete_fields = ['service']
    fields = ('service', 'start_time', 'end_time_jalali')
    readonly_fields = ('end_time_jalali',)

    def end_time_jalali(self, obj):
        if not obj.end_time:
            return "-"
        dt = localtime(obj.end_time)
        return jdatetime.datetime.fromgregorian(datetime=dt).strftime('%Y/%m/%d %H:%M')

    end_time_jalali.short_description = _('end time')

@admin.register(Appointment)
class AppointmentAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'reservation_date', 'created_at')
    list_filter = ('status','reservation_date')
    search_fields = ('customer__first_name', 'customer__last_name', 'customer__phone_number')
    inlines = [AppointmentServiceInline]
    date_hierarchy = 'reservation_date'

