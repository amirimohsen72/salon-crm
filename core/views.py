# core/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from accounts.models import Customer
from accounts.forms import CUSTOMER_ADD
from salons.mixins import SalonAccessMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import date
import jdatetime
from appointments.models import Appointment

def home(request):
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    # Get user's salon
    salon = request.user.salon
    
    # Get today's date in Gregorian
    today_gregorian = timezone.now().date()
    
    # Get today's date in Shamsi
    today_shamsi = jdatetime.date.fromgregorian(date=today_gregorian)
    today_shamsi_day = today_shamsi.day
    today_shamsi_month = today_shamsi.month
    
    # Count today's appointments (reserved and done)
    today_appointments_count = 0
    if salon:
        today_appointments_count = Appointment.objects.filter(
            salon=salon,
            reservation_date=today_gregorian,
            status__in=['reserved', 'done']
        ).count()
    
    # Count customers with birthday today (in Shamsi calendar)
    today_birthdays_count = 0
    if salon:
        # Get all customers with birth_date for this salon
        customers_with_birthday = Customer.objects.filter(
            salon=salon,
            birth_date__isnull=False
        )
        # Check each customer's birthday in Shamsi calendar
        for customer in customers_with_birthday:
            if customer.birth_date:
                customer_shamsi = jdatetime.date.fromgregorian(date=customer.birth_date)
                if customer_shamsi.day == today_shamsi_day and customer_shamsi.month == today_shamsi_month:
                    today_birthdays_count += 1
    
    context = {
        'today_appointments_count': today_appointments_count,
        'today_birthdays_count': today_birthdays_count,
    }
    return render(request, 'core/dashboard.html', context)



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