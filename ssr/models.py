from django.db import models


# Create your models here.

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(null=False, max_length=20)

    class Meta:
        db_table = "state"


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(null=False, max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        db_table = "city"


class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(null=False, max_length=20)
    area_pincode = models.CharField(null=False, max_length=6, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = "area"


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    first_name = models.CharField(null=False, max_length=20)
    last_name = models.CharField(null=False, max_length=20)
    username = models.CharField(null=False, unique=True, max_length=20)
    gender = models.CharField(null=False, max_length=6)
    cust_email = models.EmailField(null=False, unique=True, max_length=40)
    address = models.TextField(null=False, max_length=100)
    cust_contact = models.BigIntegerField(null=False, unique=True)
    password = models.CharField(null=False, max_length=20)
    is_admin = models.IntegerField(null=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    otp = models.CharField(max_length=10, null=True)
    otp_used = models.IntegerField(null=True)

    class Meta:
        db_table = "customer"


class Vehicle_Category(models.Model):
    cate_id = models.AutoField(primary_key=True)
    cate_type = models.CharField(null=False, max_length=30)
    cate_img = models.CharField(max_length=500)

    class Meta:
        db_table = "vehicle_category"


class Vehicle_Details(models.Model):
    veh_id = models.AutoField(primary_key=True)
    veh_no = models.CharField(null=False, unique=True, max_length=15)
    chassis_no = models.CharField(null=False, unique=True, max_length=20)
    rent = models.BigIntegerField(null=False)
    veh_desc = models.TextField(max_length=500)
    capacity = models.IntegerField(null=False)
    size = models.CharField(null=False, max_length=25)
    cate = models.ForeignKey(Vehicle_Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "vehicle_details"


class Driver(models.Model):
    dri_id = models.AutoField(primary_key=True)
    first_name = models.CharField(null=False, max_length=20)
    last_name = models.CharField(null=False, max_length=20)
    username = models.CharField(null=False, unique=True, max_length=20)
    gender = models.CharField(null=False, max_length=6)
    dri_email = models.EmailField(null=False, unique=True, max_length=40)
    password = models.CharField(null=False, max_length=20)
    dri_contact = models.BigIntegerField(null=False, unique=True)
    dri_license = models.CharField(null=False, unique=True, max_length=20)
    is_available = models.IntegerField(default=False, null=True)
    otp = models.CharField(max_length=10, null=True)
    otp_used = models.IntegerField(null=True)

    class Meta:
        db_table = "driver"


class Booking(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_date_time = models.DateField(null=False)
    pickup_address = models.TextField(null=False, max_length=100)
    drop_address = models.TextField(null=False, max_length=100)
    approx_km = models.IntegerField(null=False)
    amount = models.IntegerField(default=False)
    booking = models.IntegerField(null=False)
    payment_status = models.IntegerField(default=False)
    payment_type = models.IntegerField(default=False)
    cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dri = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    veh = models.ForeignKey(Vehicle_Details, on_delete=models.CASCADE)
    otp = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = "booking"


class Feedback(models.Model):
    feed_id = models.AutoField(primary_key=True)
    feed_desc = models.TextField(max_length=200)
    feed_date = models.DateField(null=False)
    cust = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = "feedback"


#class Gallery(models.Model):
#    g_id = models.AutoField(primary_key=True)
#    g_path = models.CharField(max_length=50, null=False)

#    class Meta:
#        db_table = "gallery"
