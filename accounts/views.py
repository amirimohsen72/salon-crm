from django.shortcuts import render
# from django.views.generic import CreateView
from django.views import generic
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.


# class SignUpView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     model = CustomUser
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')


class SalonLoginView(LoginView):
    template_name = 'account/login.html'