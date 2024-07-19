from django.contrib import admin
from django.urls import path
from client import client_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', client_views.client_index),
    path('client_header/', client_views.client_header),
    path('client_booking_history/', client_views.client_booking_history),
    path('client_vehicle_category/', client_views.client_vehicle_category),
    path('client_vehicle_details/<int:id>', client_views.client_vehicle_details),
    path('client_booking/<int:id>', client_views.client_booking),
    path('client_profile/', client_views.client_profile),
    path('client_register/', client_views.client_signup),
    path('client_login/', client_views.client_login),
    path('client_logout/', client_views.client_logout),
    path('client_forpass/', client_views.client_forgot_password),
    path('client_send_otp/', client_views.client_sendotp),
    path('client_set_pass/', client_views.client_set_password),
    path('client_feedback/', client_views.client_feedback),
    path('client_about_us/', client_views.client_about_us),
    path('client_contact/',client_views.client_contact),
]
