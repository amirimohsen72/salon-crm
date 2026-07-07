from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppointmentListView.as_view(), name='appointment_list'),
    path('add/', views.AppointmentCreateView.as_view(), name='appointment_add'),
    path('<int:pk>/edit/', views.AppointmentUpdateView.as_view(), name='appointment_edit'),
]