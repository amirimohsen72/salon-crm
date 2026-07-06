from django.shortcuts import render
# from django.views.generic import CreateView
from django.views import generic
from .forms import CustomUserCreationForm
from .models import CustomUser,Customer
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,PasswordChangeView,LogoutView
from django.contrib.auth.decorators import login_required
from .forms import User_Change_Info
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.


# class SignUpView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     model = CustomUser
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')


class SalonLoginView(LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = 'dashboard'

class SalonUserChangePassView(PasswordChangeView):
    template_name = 'account/password_change.html'

class SalonUserChangePassView(PasswordChangeView):
    template_name = 'account/password_change.html'

class SalonLogOutView(LogoutView):
    next_page='logedout'
    # template_name='accounts/logout'
    

# class SalonLogedOutView():
#     # next_page='logedout'
#     template_name='accounts/logout'
    
def salonlogedOut(request): 
    return render(request, 'accounts/logout.html',)



@login_required
def user_changeinfo(request):
    initial_data = {
    'first_name': request.user.first_name,
    'last_name': request.user.last_name,
    'address': request.user.address,
    'phone_number': request.user.phone_number,
  }
    # form = User_Change_Info(request.POST, initial=initial_data)
    form = User_Change_Info( initial=initial_data,)
    if request.method == 'POST':
        form = User_Change_Info(request.POST, )
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.phone_number = form.cleaned_data['phone_number']
            user.address = form.cleaned_data['address']
            user.save()

            messages.success(request, _('your info change success fully.'))
        else:
            messages.danger(request, _('your info change not submited.'))

    return render(request, 'core/change_info.html', { 'form': form, }  )
