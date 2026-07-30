from django import forms
from django.utils.translation import gettext as _
from .models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'duration', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('service name')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('description')}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('price (toman)')}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('duration (minute)')}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }