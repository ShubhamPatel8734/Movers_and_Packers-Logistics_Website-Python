from django import forms
from ssr.models import State, City, Area, Customer, Vehicle_Category, Vehicle_Details, Driver, Booking, Feedback
from parsley.decorators import parsleyfy

@parsleyfy
class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ["state_name"]


@parsleyfy
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["city_name", "state"]


@parsleyfy
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ["area_name", "area_pincode", "city"]


@parsleyfy
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "username", "gender", "cust_email", "address", "cust_contact", "password",
                  "is_admin", "area"]


@parsleyfy
class Vehicle_CategoryForm(forms.ModelForm):
    cate_img = forms.FileField()
    class Meta:
        model = Vehicle_Category
        fields = ["cate_type", "cate_img"]


@parsleyfy
class Vehicle_DetailsFrom(forms.ModelForm):
    class Meta:
        model = Vehicle_Details
        fields = ["veh_no", "chassis_no", "rent", "veh_desc", "capacity", "size", "cate"]


@parsleyfy
class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["first_name", "last_name", "username", "gender", "dri_email", "password", "dri_contact",
                  "dri_license", "is_available"]


@parsleyfy
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["book_date_time", "pickup_address", "drop_address", "approx_km", "cust", "veh"]


@parsleyfy
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["feed_desc", "feed_date", "cust"]


@parsleyfy
class UpdateImgForm(forms.ModelForm):
    cate_img = forms.FileField()
    class Meta:
        model = Vehicle_Category
        fields = ["cate_img"]

