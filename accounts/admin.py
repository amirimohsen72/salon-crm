from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUser , Customer
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','age','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('age','phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields' : ('age' ,'phone_number' )}),
    )


admin.site.register(CustomUser,CustomUserAdmin)



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone_number', 'is_active','created_at')
    list_filter = ('is_active',)
    search_fields = ('phone_number','last_name', 'first_name',)
