from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.translation import gettext as _

from salons.mixins import SalonAccessMixin
from .models import Appointment, AppointmentService
from .forms import AppointmentForm, AppointmentServiceForm, AppointmentServiceFormSet
from services.models import Service


class AppointmentListView(SalonAccessMixin, ListView):
    template_name = 'appointments/appointmentlist.html'
    model = Appointment

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by status
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)

        # Filter by date range
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        if date_from:
            queryset = queryset.filter(reservation_date__gte=date_from)
        if date_to:
            queryset = queryset.filter(reservation_date__lte=date_to)

        return queryset.select_related('customer').prefetch_related('services__service')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_filter'] = self.request.GET.get('status', '')
        context['date_from'] = self.request.GET.get('date_from', '')
        context['date_to'] = self.request.GET.get('date_to', '')
        return context


class AppointmentCreateView(SalonAccessMixin, CreateView):
    template_name = 'appointments/appointment_add.html'
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy('appointment_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['service_formset'] = AppointmentServiceFormSet(
                self.request.POST,
                instance=self.object,
                form_kwargs={'user': self.request.user}
            )
        else:
            context['service_formset'] = AppointmentServiceFormSet(
                instance=self.object,
                form_kwargs={'user': self.request.user}
            )
        return context

    def form_valid(self, form):
        form.instance.salon = self.request.user.salon
        self.object = form.save()

        # Handle the formset
        context = self.get_context_data()
        service_formset = context['service_formset']
        if service_formset.is_valid():
            service_formset.instance = self.object
            service_formset.save()
        else:
            return self.render_to_response(self.get_context_data(form=form))

        return redirect(self.success_url)


class AppointmentUpdateView(SalonAccessMixin, UpdateView):
    template_name = 'appointments/appointment_edit.html'
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy('appointment_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['service_formset'] = AppointmentServiceFormSet(
                self.request.POST,
                instance=self.object,
                form_kwargs={'user': self.request.user}
            )
        else:
            context['service_formset'] = AppointmentServiceFormSet(
                instance=self.object,
                form_kwargs={'user': self.request.user}
            )
        return context

    def form_valid(self, form):
        self.object = form.save()

        # Handle the formset
        context = self.get_context_data()
        service_formset = context['service_formset']
        if service_formset.is_valid():
            service_formset.instance = self.object
            service_formset.save()
        else:
            return self.render_to_response(self.get_context_data(form=form))

        return redirect(self.success_url)