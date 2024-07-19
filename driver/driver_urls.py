from django.contrib import admin
from django.urls import path
from driver import driver_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('driver/', driver_views.driver_index),
    path('driver_register/', driver_views.driver_register),
    path('driver_login/', driver_views.driver_login),
    path('driver_logout/', driver_views.driver_logout),
    path('driver_forgot_password/', driver_views.driver_forgot_password),
    path('driver_send_otp/', driver_views.driver_sendotp),
    path('driver_set_pass/', driver_views.driver_set_password),
    path('driver_profile/', driver_views.driver_profile),
    path('driver_edit_profile/', driver_views.driver_edit_profile),
    path('driver_booking_complete/<int:id>', driver_views.driver_booking_complete),
    path('driver_bookings/',driver_views.driver_bookings),
]
