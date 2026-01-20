from django.contrib import admin, messages
from .models import Appointment, AppointmentService
from jalali_date.admin import ModelAdminJalaliMixin
from django.utils.translation import gettext as _
from django.utils.timezone import localtime
from jalali_date import jdatetime, datetime2jalali, date2jalali
from notifications.services import send_sms


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



@admin.action(description=_('remember appointment send sms'))
def send_reminder_sms(modeladmin, request, queryset):
    # sms_service = SMSService()
    success_count = 0
    fail_count = 0
    for appointment in queryset:
        customer = appointment.customer
        if not customer.phone_number:
            fail_count += 1
            continue

        services_qs = appointment.services.select_related('service')
        services_names = '، '.join(
            s.service.name for s in services_qs
        )
        first_service = services_qs.first()
        print(first_service)

        context = {
            'name': f"{customer.first_name} {customer.last_name}" ,
            'date': date2jalali(appointment.reservation_date).strftime('%Y/%m/%d'),
            'time': datetime2jalali(first_service.start_time).strftime('%H:%M') if first_service else '',
            'services': services_names,
        }
        sms_log = send_sms(
            phone_number=customer.phone_number,
            template_type='appointment_reminder',
            context=context,
            customer=customer,
            appointment=appointment,
        )
        if sms_log and sms_log.status == sms_log.Status.SENT:
            success_count += 1
        else:
            fail_count += 1
    if success_count:
        messages.success(
            request,
            f'{success_count} پیامک با موفقیت ارسال شد'
        )
    if fail_count:
        messages.warning(
            request,
            f'{fail_count} پیامک ارسال نشد'
        )


@admin.register(Appointment)
class AppointmentAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'reservation_date', 'created_at')
    list_filter = ('status','reservation_date')
    search_fields = ('customer__first_name', 'customer__last_name', 'customer__phone_number')
    inlines = [AppointmentServiceInline]
    date_hierarchy = 'reservation_date'
    actions = [send_reminder_sms]


