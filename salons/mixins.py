from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import admin
from django.db.models import Q
from django.views.generic.list import MultipleObjectMixin
 

# ------------------------------------------- Salon Access Mixin -----------------------------------------
class SalonAccessMixin(LoginRequiredMixin):
    """Mixin that requires login and filters queryset to user's salon"""

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(salon=self.request.user.salon)
