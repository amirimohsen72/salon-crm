from django import forms
from django.utils.translation import gettext as _
from django.utils import timezone
from .models import Appointment, AppointmentService
from accounts.models import Customer
from services.models import Service


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['customer', 'reservation_date', 'note', 'status']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'reservation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('note')}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            # Only active customers belonging to this salon
            self.fields['customer'].queryset = Customer.objects.filter(
                salon=user.salon, is_active=True
            )
            self.fields['customer'].label_from_instance = lambda obj: f"{obj.get_full_name()} ({obj.phone_number})"

    def clean_reservation_date(self):
        date = self.cleaned_data.get('reservation_date')
        if date and date < timezone.now().date():
            raise forms.ValidationError(_("Reservation date cannot be in the past"))
        return date


class AppointmentServiceForm(forms.ModelForm):
    class Meta:
        model = AppointmentService
        fields = ['service', 'start_time']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            # Only active services belonging to this salon
            self.fields['service'].queryset = Service.objects.filter(
                salon=user.salon, active=True
            )

    def clean_start_time(self):
        start_time = self.cleaned_data.get('start_time')
        if start_time and start_time < timezone.now():
            raise forms.ValidationError(_("Start time cannot be in the past"))
        return start_time