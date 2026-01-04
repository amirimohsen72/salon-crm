
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
# user creattion form -> signup
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields =  ('first_name','last_name','username','age', 'email', )

# user change form -> admin panel

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields =  ('first_name','last_name','username','age', 'email', )