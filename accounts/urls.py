from django.urls import path
from . import views

urlpatterns = [
    # path( 'signup/', views.SignUpView.as_view() , name='signup' ),
    path( 'login/', views.SalonLoginView.as_view() , name='login' ),
    path( 'logout/', views.SalonLogOutView.as_view() , name='logout' ),
    path( 'logedout', views.salonlogedOut , name='logedout' ),
    path( 'changepass/', views.SalonUserChangePassView.as_view() , name='account_change_password' ),
    path('edit_info/', views.user_changeinfo, name='change_info'),

]
