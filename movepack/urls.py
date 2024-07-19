"""movepack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ssr import views
# from django.conf.urls import url
from django.urls import include, re_path as url

from ssr.views import HomeView, ChartData

urlpatterns = [
    url(r'home', HomeView.as_view(), name='home'),
    url(r'^api/chart/data/$', ChartData.as_view(), name="api-data"),

    path('admin/', admin.site.urls),
    path('show/', views.show),
    path('profile/', views.profile),
    path('edit_profile/', views.edit_profile),
    path('state/', views.state),
    path('city/', views.city),
    path('area/', views.area),
    path('customer/', views.customer),
    path('vehicle_category/', views.vehicle_category),
    path('vehicle_details/', views.vehicle_details),
    path('driver1/<int:id>', views.driver1),
    path('booking/', views.booking),
    path('feedback/', views.feedback),
    path('d_state/<int:id>', views.dest_state),
    path('d_city/<int:id>', views.dest_driver),
    path('d_area/<int:id>', views.dest_area),
    path('d_customer/<int:id>', views.dest_customer),
    path('d_vehicle_category/<int:id>', views.dest_vehicle_category),
    path('d_vehicle_details/<int:id>', views.dest_vehicle_details),
    path('d_driver/<int:id>', views.dest_driver),
    path('d_booking/<int:id>', views.dest_booking),
    path('d_feedback/<int:id>', views.dest_feedback),
    path('index/', views.dashboard),
    path('login/', views.login),
    path('logout/', views.logout),
    path('i_state/', views.insert_state),
    path('i_vehicle_category/', views.insert_vehicle_category),
    path('i_city/', views.insert_city),
    path('i_area/', views.insert_area),
    path('i_vehicle_details/', views.insert_vehicle_details),
    path('u_state/<int:id>', views.update_state),
    path('u_vehicle_category/<int:id>', views.update_vehicle_category),
    path('u_city/<int:id>', views.update_city),
    path('u_area/<int:id>', views.update_area),
    path('u_vehicle_details/<int:id>', views.update_vehicle_details),
    # path('upload/', views.upload_image),
    path('forgot_password/', views.forgot_password),
    path('send_otp/', views.sendotp),
    path('set_pass/', views.set_password),
    path('accept_booking/<int:id>', views.accept_booking),
    path('reject_booking/<int:id>', views.reject_booking),
    path('allocate_driver/<int:id>', views.allocate_driver),
    path('update_image/<int:id>', views.update_image),
    path('report1/', views.static_report),
    path('report2/',views.datewise_report),
    path('report3/',views.vehicle_report),
    path('report4/',views.userwise_report),
    path('report5/',views.payment_report),

    path('client/', include('client.client_urls')),

    path('driver/', include('driver.driver_urls')),

]
