from django.urls import path
from .views import home,dashboard,CustomerListView,CreateCustomerView, CustomerUpdateView

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),

    path( 'customers/', CustomerListView.as_view() , name='customer_list' ),
    path( 'customer/add', CreateCustomerView.as_view() , name='customer_add' ),
    path( 'customer/<int:pk>/edit/', CustomerUpdateView.as_view() , name='customer_edit' ),
    ]
