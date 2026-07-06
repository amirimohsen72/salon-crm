
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser,Customer
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django import forms


# user creattion form -> signup
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields =  ('first_name','last_name','username','age', 'email', 'salon', )

# user change form -> admin panel

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields =  ('first_name','last_name','username','age', 'email', 'salon',)




class User_Change_Info(forms.ModelForm):
    class Meta:
        model = get_user_model()
        # fields = ['first_name', 'last_name', 'phone_number', 'Address']
        fields = ['first_name', 'last_name', 'phone_number','salon', ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': _('first name'), 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': _('last name'), 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': _('phone number'), 'class': 'form-control'}),
            # 'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            #     'order_note': forms.Textarea(attrs={
            #         'rows': 5,
            #         'placeholder': 'If you have any notes please enter here otherwise leave it empty.',
            #         'class': 'form-control'
            #     }),
        }




class CUSTOMER_ADD(forms.ModelForm):
    class Meta:
        model = Customer
        # fields = ['first_name', 'last_name', 'phone_number', 'Address']
        fields = ['first_name', 'last_name', 'phone_number', 'birth_date', 'birth_month', 'note', ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': _('first name'), 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': _('last name'), 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': _('phone number'), 'class': 'form-control'}),
            #     'note': forms.Textarea(attrs={
            #         'rows': 3 ,
            #         'placeholder': 'If you have any notes please enter here otherwise leave it empty.',
            #         'class': 'form-control'
            #     }),
        }
