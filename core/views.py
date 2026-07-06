# core/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from accounts.models import Customer
from accounts.forms import CUSTOMER_ADD
from salons.mixins import SalonAccessMixin
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')



class CustomerListView(SalonAccessMixin, ListView):
    template_name= 'accounts/customerlist.html'
    model= Customer

class CreateCustomerView(LoginRequiredMixin, CreateView):
    template_name= 'accounts/addcustomer.html'
    model= Customer
    form_class = CUSTOMER_ADD
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        # Set the salon from the logged-in user
        form.instance.salon = self.request.user.salon
        return super().form_valid(form)


class CustomerUpdateView(SalonAccessMixin, UpdateView):
    template_name = 'accounts/customeredit.html'
    model = Customer
    form_class = CUSTOMER_ADD
    success_url = reverse_lazy('customer_list')