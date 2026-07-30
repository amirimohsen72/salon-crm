from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServiceListView.as_view(), name='service_list'),
    path('add/', views.ServiceCreateView.as_view(), name='service_add'),
    path('<int:pk>/edit/', views.ServiceUpdateView.as_view(), name='service_edit'),
    path('<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),
]