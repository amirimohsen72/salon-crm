from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.utils.translation import gettext as _

from salons.mixins import SalonAccessMixin
from .models import Service
from .forms import ServiceForm


class ServiceListView(SalonAccessMixin, ListView):
    template_name = 'services/servicelist.html'
    model = Service
    context_object_name = 'services'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Annotate with count of related appointments for template logic
        from django.db.models import Count
        return queryset.annotate(appointment_count=Count('appointmentservice'))


class ServiceCreateView(SalonAccessMixin, CreateView):
    template_name = 'services/service_add.html'
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('service_list')

    def form_valid(self, form):
        form.instance.salon = self.request.user.salon
        messages.success(self.request, _('Service created successfully.'))
        return super().form_valid(form)


class ServiceUpdateView(SalonAccessMixin, UpdateView):
    template_name = 'services/service_edit.html'
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('service_list')

    def form_valid(self, form):
        messages.success(self.request, _('Service updated successfully.'))
        return super().form_valid(form)


class ServiceDeleteView(SalonAccessMixin, DeleteView):
    model = Service
    template_name = 'services/service_confirm_delete.html'
    success_url = reverse_lazy('service_list')
    context_object_name = 'service'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Check if service has related appointments
        if self.object.appointmentservice_set.exists():
            messages.error(
                self.request,
                _('Cannot delete this service because it has related appointments. '
                  'Please remove the related appointments first.')
            )
            return redirect(self.success_url)
        messages.success(self.request, _('Service deleted successfully.'))
        return super().delete(request, *args, **kwargs)
