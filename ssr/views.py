import sys
import datetime

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date

from movepack import settings
from ssr.models import State, City, Area, Customer, Vehicle_Category, Vehicle_Details, Driver, Booking, Feedback
from ssr.forms import *

from django.db import connection

from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

from ssr.function import handle_uploaded_file


# Create your views here.


def show(request):
    print("*************************")
    id1 = request.session['admin_id']
    ad = Customer.objects.get(cust_id=id1)
    return render(request, "header.html", {'ad': ad})


def dashboard(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
        u = Customer.objects.all().count()
        c = Vehicle_Category.objects.all().count()
        b = Booking.objects.all().count()
        date = datetime.date.today()
        bo = Booking.objects.filter(book_date_time=date)
        vc = Vehicle_Category.objects.all()
        return render(request, "index.html", {"user": u, "cat": c, "book": b, 'ad': ad, 'vc': vc, 'bo': bo})
    else:
        return redirect("/login")


def profile(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
        return render(request, "admin_profile.html", {'ad': ad, 'id1': id1})
    else:
        return redirect("/login")


def edit_profile(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
        ar = Area.objects.all()

        form = CustomerForm(request.POST, instance=ad)
        print("-----------***************---------", form.errors)
        if form.is_valid():
            print("*****************************")
            try:
                form.save()
                return redirect("/profile/")
            except:
                print("---------------", sys.exc_info())

        return render(request, "admin_edit_profile.html", {'ad': ad, 'ar': ar, 'id1': id1})
    else:
        return redirect("/login")


# def edit_picture(request):
#     if 'admin_id' in request.session:
#         id1 = request.session['admin_id']
#         ad = Customer.objects.get(cust_id=id1)
#
#         form = CustomerForm(request.POST, instance=ad.cust_img)
#         print("-----------***************---------", form.errors)
#         if form.is_valid():
#             print("*****************************")
#             try:
#                 form.save()
#                 return redirect("/profile/")
#             except:
#                 print("---------------", sys.exc_info())
#
#         return render(request, "admin_edit_profile.html", {'ad': ad, 'id1': id1})
#     else:
#         return redirect("/login")


def state(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
        st = State.objects.all()
        return render(request, "state.html", {'st': st, 'ad': ad})
    else:
        return redirect("/login")


def city(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    ci = City.objects.all()
    st = State.objects.all()
    return render(request, "city.html", {'ci': ci, 'st': st, 'ad': ad})


def area(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    ar = Area.objects.all()
    return render(request, "area.html", {'ar': ar, 'ad': ad})


def customer(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    cu = Customer.objects.all()
    return render(request, "customer.html", {'cu': cu, 'ad': ad})


def vehicle_category(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    vc = Vehicle_Category.objects.all()
    return render(request, "vehicle_category.html", {'vc': vc, 'ad': ad})


def vehicle_details(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    vd = Vehicle_Details.objects.all()
    return render(request, "vehicle_details.html", {'vd': vd, 'ad': ad})


# def driver(request):
#     if 'admin_id' in request.session:
#         id1 = request.session['admin_id']
#         ad = Customer.objects.get(cust_id=id1)
#     else:
#         return redirect("/login")
#     dr = Driver.objects.all()
#     date = datetime.date.today()
#     return render(request, "driver.html", {'dr': dr, 'ad': ad, 'date': date})


def driver1(request, id):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    bid = id
    dr = Driver.objects.all()
    return render(request, "driver.html", {'dr': dr, 'ad': ad, 'bid': bid})


def booking(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    bo = Booking.objects.all().order_by('-book_id')
    dr = Driver.objects.all()
    date = datetime.date.today()
    return render(request, "booking.html", {'bo': bo, 'ad': ad, 'dr': dr, 'date': date})


def feedback(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    fe = Feedback.objects.all().order_by('-feed_id')
    return render(request, "feedback.html", {'fe': fe, 'ad': ad})


# destroy functions .....

def dest_state(request, id):
    st1 = State.objects.get(state_id=id)
    st1.delete()
    return redirect("/state")


def dest_city(request, id):
    ci1 = City.objects.get(city_id=id)
    ci1.delete()
    return redirect("/city")


def dest_area(request, id):
    ar1 = Area.objects.get(area_id=id)
    ar1.delete()
    return redirect("/city")


def dest_customer(request, id):
    cu1 = Customer.objects.get(cust_id=id)
    cu1.delete()
    return redirect("/customer")


def dest_vehicle_category(request, id):
    vc1 = Vehicle_Category.objects.get(cate_id=id)
    vc1.delete()
    return redirect("/vehicle_category")


def dest_vehicle_details(request, id):
    vd1 = Vehicle_Details.objects.get(veh_id=id)
    vd1.delete()
    return redirect("/vehicle_details")


def dest_driver(request, id):
    dr1 = Driver.objects.get(dri_id=id)
    dr1.delete()
    return redirect("/driver")


def dest_booking(request, id):
    bo1 = Booking.objects.get(book_id=id)
    bo1.delete()
    return redirect("/booking")


def dest_feedback(request, id):
    fe1 = Feedback.objects.get(feed_id=id)
    fe1.delete()
    return redirect("/feedback")


from ssr.models import Customer


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {"customers": 10})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # qs = Company.objects.all()

        cursor = connection.cursor()
        print('-----------------'),
        cursor.execute(
            '''SELECT (select cate_type from vehicle_category where cate_id = v.cate_id) as name, sum(amount) as total FROM booking b join vehicle_details v where b.veh_id = v.veh_id group by b.veh_id;;''')
        qs = cursor.fetchall()

        labels = []
        default_items = []

        for item in qs:
            labels.append(item[0])
            default_items.append(item[1])

        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = Customer.objects.filter(cust_email=email, password=password, is_admin=0).count()
        print("-------------------", email, "---------------------", password, "========", val)
        if val == 1:
            udata = Customer.objects.filter(cust_email=email, password=password, is_admin=0)
            for item in udata:
                request.session['admin_email'] = item.cust_email
                request.session['admin_pass'] = item.password
                request.session['admin_id'] = item.cust_id
                if request.POST.get("remember"):
                    response = redirect('/index/')
                    response.set_cookie('A_admin_email', request.POST['email'], 3600 * 24 * 365 * 2)
                    response.set_cookie('A_admin_pass', request.POST['password'], 3600 * 24 * 365 * 2)
                    return response
            return redirect('/index/')
        else:
            messages.error(request, "Invalid Email or password")
            return redirect('/login/')
    else:
        if request.COOKIES.get("A_admin_email"):
            return render(request, "admin_login.html", {'admin_email_cookie1': request.COOKIES['A_admin_email'],
                                                        'admin_password_cookie2': request.COOKIES['A_admin_pass']})
        else:
            return render(request, "admin_login.html")


def logout(request):
    try:
        del request.session['admin_email']
        del request.session['admin_pass']
        del request.session['admin_id']
    except:
        pass

    return redirect('/login')


# insert functions .....

def insert_state(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    if request.method == "POST":
        form = StateForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/state")
            except:
                print("--------", sys.exc_info())
    else:
        form = StateForm()
    return render(request, "state_insert.html", {'form': form, 'ad': ad})


def insert_vehicle_category(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login/")
    if request.method == "POST":
        form = Vehicle_CategoryForm(request.POST, request.FILES)
        print("---------", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['cate_img'])
                form.save()
                return redirect("/vehicle_category/")
            except:
                print("--------", sys.exc_info())
    else:
        form = Vehicle_CategoryForm()
    return render(request, "vehicle_category_insert.html", {'form': form, 'ad': ad})


def insert_city(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    st = State.objects.all()
    if request.method == "POST":
        form = CityForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/city")
            except:
                print("--------", sys.exc_info())
    else:
        form = CityForm()
    return render(request, "city_insert.html", {'form': form, 'st': st, 'ad': ad})


def insert_area(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    ci = City.objects.all()
    if request.method == "POST":
        form = AreaForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/area")
            except:
                print("--------", sys.exc_info())
    else:
        form = AreaForm()
    return render(request, "area_insert.html", {'form': form, 'ci': ci, 'ad': ad})


def insert_vehicle_details(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    vc = Vehicle_Category.objects.all()
    if request.method == "POST":
        form = Vehicle_DetailsFrom(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/vehicle_details")
            except:
                print("--------", sys.exc_info())
    else:
        form = Vehicle_DetailsFrom()

    return render(request, "vehicle_details_insert.html", {'form': form, 'vc': vc, 'ad': ad})


# def upload_image(request):
#     if request.method == 'POST':
#         g = Vehicle_DetailsFrom(request.POST, request.FILES)
#         print("____", g.errors)
#         if g.is_valid():
#             try:
#                 handle_uploaded_file(request.FILES['cate_img '])
#                 g.save()
#                 return HttpResponse("File Uploaded Successfully...")
#             except:
#                 print("---------------", sys.exc_info())
#     else:
#         g = Vehicle_DetailsFrom()
#         return render(request, "vehicle_details_insert.html", {'form': g})


def update_state(request, id):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    state = State.objects.get(state_id=id)
    form = StateForm(request.POST, instance=state)

    if form.is_valid():
        try:
            form.save()
            return redirect("/state")
        except:
            print("---------------", sys.exc_info())

    return render(request, "state_edit.html", {'state': state, 'ad': ad})


def update_vehicle_category(request, id):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    vehicle_category = Vehicle_Category.objects.get(cate_id=id)
    form = Vehicle_CategoryForm(request.POST, instance=vehicle_category)

    if form.is_valid():
        try:
            form.save()
            return redirect("/vehicle_category")
        except:
            print("---------------", sys.exc_info())

    return render(request, "vehicle_category_edit.html", {'vehicle_category': vehicle_category, 'ad': ad})


def update_city(request, id):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    city = City.objects.get(city_id=id)
    form = CityForm(request.POST, instance=city)
    st = State.objects.all()

    if form.is_valid():
        try:
            form.save()
            return redirect("/city")
        except:
            print("---------------", sys.exc_info())

    return render(request, "city_edit.html", {'city': city, 'st': st, 'ad': ad})


def update_area(request, id):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    area = Area.objects.get(area_id=id)
    form = AreaForm(request.POST, instance=area)
    ci = City.objects.all()

    if form.is_valid():
        try:
            form.save()
            return redirect("/area")
        except:
            print("---------------", sys.exc_info())

    return render(request, "area_edit.html", {'area': area, 'ci': ci, 'ad': ad})


def update_vehicle_details(request, id):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
    else:
        return redirect("/login")
    vehicle_details = Vehicle_Details.objects.get(veh_id=id)
    form = Vehicle_DetailsFrom(request.POST, instance=vehicle_details)
    vc = Vehicle_Category.objects.all()

    if form.is_valid():
        try:
            form.save()
            return redirect("/vehicle_details")
        except:
            print("---------------", sys.exc_info())

    return render(request, "vehicle_details_edit.html", {'vehicle_details': vehicle_details, 'vc': vc, 'ad': ad})


from django.core.mail import send_mail
import random


def sendotp(request):
    otp1 = random.randint(10000, 99999)
    e = request.POST['email']

    request.session['temail'] = e

    obj = Customer.objects.filter(cust_email=e).count()

    if obj == 1:
        val = Customer.objects.filter(cust_email=e).update(otp=otp1, otp_used=0)

        subject = 'OTP Verification'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, 'set_password.html')


def forgot_password(request):
    return render(request, "admin_forgot.html")


def set_password(request):
    if request.method == "POST":

        T_otp = request.POST['otp']
        T_pass = request.POST['password']
        T_cpass = request.POST['cpassword']

        if T_pass == T_cpass:

            e = request.session['temail']
            val = Customer.objects.filter(cust_email=e, otp=T_otp, otp_used=0).count()

            if val == 1:
                Customer.objects.filter(cust_email=e).update(otp_used=1, password=T_pass)
                return redirect("/login")
            else:
                messages.error(request, "Invalid OTP")
                return render(request, "admin_forgot.html")

        else:
            messages.error(request, "New password and Confirm password does not match ")
            return render(request, "set_password.html")

    else:
        return redirect("/forgot_password")


def accept_booking(request, id):
    otp1 = random.randint(1000000, 9999999)
    b = Booking.objects.get(book_id=id)
    b.booking = '1'
    b.otp = str(otp1)
    b.save()
    e = b.cust.cust_email
    print("--------------------------------", e)
    subject = 'Booking Status'
    message = f'Dear {b.cust.first_name} {b.cust.last_name}, We have accept your booking, we contact you soon.' \
              f'your booking verification id is {otp1}'

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [e, ]
    send_mail(subject, message, email_from, recipient_list)
    return redirect('/booking/')


def allocate_driver(request, id):
    print("***********-----------------************")
    if request.method == "POST":
        bid = request.POST.get("book_id")
        print("-------------//////////------", bid, "**********", id)
        b = Booking.objects.get(book_id=bid)
        b.dri_id = id
        b.save()
        d = Driver.objects.get(dri_id=id)
        d.is_available = 1
        d.save()

        if b.payment_type == 2:
            pay_type = b.amount
        else:
            pay_type = 'None'

        e = b.dri.dri_email
        print("------------------------------", e)
        subject = "Your Today's Booking"
        message = f"Dear {b.dri.first_name} {b.dri.last_name}, Your today's booking details are :- \n \n Customer's Name : {b.cust.first_name} {b.cust.last_name} \n Customer's Contact : {b.cust.cust_contact} \n Pickup Address : {b.pickup_address} \n Drop Address : {b.drop_address} \n Payment Cash on Delivery : ₹{pay_type} \n Allotted Vehicle : {b.veh.cate.cate_type}"

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]
        send_mail(subject, message, email_from, recipient_list)

        c_e = b.cust.cust_email
        print("++++++++++++++++++++++++++++++", c_e)
        c_subject = "Your Driver Details"
        c_message = f"Dear {b.cust.first_name} {b.cust.last_name}, Your Driver Details are :- \n \n Driver's Name : {b.dri.first_name} {b.dri.last_name} \n Driver's Contact : {b.dri.dri_contact}"

        c_email_from = settings.EMAIL_HOST_USER
        c_recipient_list = [c_e, ]
        send_mail(c_subject, c_message, c_email_from, c_recipient_list)
        return redirect('/booking/')
    return redirect('/driver/')


def reject_booking(request, id):
    b = Booking.objects.get(book_id=id)
    b.booking = '2'
    b.save()
    if b.payment_status == 1:
        e = b.cust.cust_email
        print("--------------------------------", e)
        subject = 'Booking Status'
        message = f'Dear {b.cust.first_name} {b.cust.last_name}, Your booking is rejected by the owner due to some resone, Soory for that.' \
                  f'Visit again.'

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]
        send_mail(subject, message, email_from, recipient_list)
    else:
        e = b.cust.cust_email
        print("--------------------------------", e)
        subject = 'Booking Status'
        message = f'Dear {b.cust.first_name} {b.cust.last_name}, We have regret to inform you, your order has been rejected  due to some technical issue. ' \
                  f'We will refund your amount in 2/3 days '

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]
        send_mail(subject, message, email_from, recipient_list)
    return redirect('/booking/')


def update_image(request, id):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
        vc = Vehicle_Category.objects.get(cate_id=id)

        if request.method == "POST":
            form = UpdateImgForm(request.POST, request.FILES, instance=vc)
            print("-------------------", form.errors)

            if form.is_valid():
                try:
                    handle_uploaded_file(request.FILES['cate_img'])
                    form.save()
                    return redirect('/vehicle_category/')

                except:
                    print('------------------------', sys.exc_info())

        else:
            form = Vehicle_CategoryForm()

        return render(request, "updateimage.html", {'form': form, 'ad': ad, 'vehicle_category': vc})
    else:
        return render(request, "admin_login.html")


def static_report(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
        sql = "SELECT 1 as book_id, (select cate_type from vehicle_category where cate_id = v.cate_id) as name, sum(amount) as total FROM booking b join vehicle_details v where b.veh_id = v.veh_id group by b.veh_id;"
        b = Booking.objects.raw(sql)
        print("=============", b)
        return render(request, "static_report.html", {"b": b, 'ad': ad})
    else:
        return redirect("/login")


def datewise_report(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
        if request.method == "POST":
            s_d = request.POST.get('start_date')
            e_d = request.POST.get('end_date')
            start = parse_date(s_d)
            end = parse_date(e_d)
            bo = Booking.objects.filter(book_date_time__range=[start, end])
            # sql = "SELECT * FROM order_table o JOIN order_item i where o.order_id = i.order_id_id and o.order_date >= %s and o.order_date <= %s;"
            # ord = Order_item.objects.raw(sql,[s_d,e_d])
        else:
            bo = Booking.objects.all()
        return render(request, "datewise_report.html", {"bo": bo, "ad": ad})
    else:
        return redirect("/login")


# def report3(request):


def vehicle_report(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
        vd = Vehicle_Details.objects.all()
        if request.method == "POST":
            id = request.POST.get('veh_id')
            vc = Booking.objects.filter(veh_id=id)
        else:
            vc = Booking.objects.all()
        return render(request, "vehicle_report.html", {'vc': vc, 'vd': vd, 'ad': ad})
    else:
        return redirect("/login")


def userwise_report(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
        cu = Customer.objects.filter(is_admin=1)
        if request.method == "POST":
            id = request.POST.get('cust_id')
            bo = Booking.objects.filter(cust_id=id)
        else:
            bo = Booking.objects.all()
        return render(request, "customer_report.html", {'bo': bo, 'cu': cu, 'ad': ad})
    else:
        return redirect("/login")


def payment_report(request):
    if 'admin_id' in request.session:
        id1 = request.session['admin_id']
        ad = Customer.objects.get(cust_id=id1)
        cu = Customer.objects.filter(is_admin=1)
        if request.method == "POST":
            type = request.POST.get('payment_type')
            bo = Booking.objects.filter(payment_type=type)
        else:
            bo = Booking.objects.all()
        return render(request, "payment_report.html", {'bo': bo, 'cu': cu, 'ad': ad})
    else:
        return redirect("/login")

