import datetime
import sys

from django.db.models import Sum
from django.shortcuts import render, redirect

from movepack import settings
from ssr.forms import *
from ssr.models import *
from django.contrib import messages


# Create your views here.

def client_index(request):
    if 'client_id' in request.session:
        id1 = request.session['client_id']
        cu = Customer.objects.get(cust_id=id1)

        fe = Feedback.objects.all()
        cust = Customer.objects.all().count()
        bo = Booking.objects.all().count()
        book = Booking.objects.filter(booking=1).count()
        print("===-==-=-=-=-=-=-=", book)
        ca = Booking.objects.aggregate(total=Sum('amount'))
        ca = ca['total']
        print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*", ca)
        return render(request, "client_index.html",
                      {'cu': cu, 'fe': fe, 'cust': cust, 'bo': bo, 'book': book, 'ca': ca})
    else:
        fe = Feedback.objects.all()
        cust = Customer.objects.all().count()
        bo = Booking.objects.all().count()
        book = Booking.objects.filter(booking=1).count()
        print("===-==-=-=-=-=-=-=", book)
        ca = Booking.objects.aggregate(total=Sum('amount'))
        ca = ca['total']
        print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*", ca)
        return render(request, "client_index.html", {'fe': fe, 'cust': cust, 'bo': bo, 'book': book, 'ca': ca})


def client_header(request):
    print("*************************")
    id1 = request.session['client_id']
    cu = Customer.objects.get(cust_id=id1)
    return render(request, "client_header.html", {'cu': cu})


import razorpay


def ch(request):
    if request.method == 'POST':
        amount = 100
        currency = 'INR'
        client = razorpay.Client(auth=("rzp_test_NUypu1AHXILZ3L", "oYuOpyGwDe2e60P8IMKk67h2"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return render(request, 'client_booking_history.html')


def client_booking_history(request):
    if 'client_id' in request.session:
        id1 = request.session['client_id']
        cu = Customer.objects.get(cust_id=id1)
        bo = Booking.objects.filter(cust=id1).order_by('-book_id')

        if request.method == "POST":
            id = request.POST.get('id')
            print("66666666666666666666666666666666666666666666666", id)
            Booking.objects.filter(cust=id1, book_id=id).update(payment_status=1)
        return render(request, "client_booking_history.html", {'bo': bo, 'cu': cu})
    else:
        return redirect("/client/client_login")


def client_vehicle_category(request):
    if 'client_id' in request.session:
        id1 = request.session['client_id']
        cu = Customer.objects.get(cust_id=id1)
        vc = Vehicle_Category.objects.all()
        return render(request, "client_vehicle_category.html", {'vc': vc, 'cu': cu})
    else:
        vc = Vehicle_Category.objects.all()
        return render(request, "client_vehicle_category.html", {'vc': vc})


def client_vehicle_details(request, id):
    if 'client_id' in request.session:
        id1 = request.session['client_id']
        cu = Customer.objects.get(cust_id=id1)
        vc = Vehicle_Category.objects.all()
        vcid = Vehicle_Category.objects.get(cate_id=id)
        vd = Vehicle_Details.objects.get(veh_id=id)
        return render(request, "client_vehicle_details.html", {'vc': vc, 'vd': vd, 'cu': cu, 'vcid': vcid})
    else:
        vc = Vehicle_Category.objects.all()
        vcid = Vehicle_Category.objects.get(cate_id=id)
        vd = Vehicle_Details.objects.get(veh_id=id)
        return render(request, "client_vehicle_details.html", {'vc': vc, 'vd': vd, 'vcid': vcid})


def client_booking(request, id):
    if 'client_id' in request.session:
        id1 = request.session['client_id']
        cu = Customer.objects.get(cust_id=id1)
        vd = Vehicle_Details.objects.get(veh_id=id)
        vid = str(id)
        print("============================", id1)
        date = str(datetime.date.today())
        if request.method == "POST":
            bd = request.POST.get("book_date_time")
            pa = request.POST.get("pickup_address")
            da = request.POST.get("drop_address")
            appkm = request.POST.get('approx_km')
            pt = request.POST.get("payment_type")
            v = Vehicle_Details.objects.filter(veh_id=id)
            for data in v:
                r = data.rent
                print("rent=", r)
            t = int(appkm) * int(r)
            t1 = float(t)
            print("************", bd, pa, da, appkm, t)
            b = Booking(book_date_time=bd, pickup_address=pa, drop_address=da, approx_km=appkm, amount=t1, booking=0,
                        payment_status=0, payment_type=pt,
                        cust_id=id1, dri_id=None, veh_id=id)
            b.save()
            return redirect("/client/client_booking_history/")
        return render(request, "client_booking.html",
                      {'id1': id1, 'date': date, 'vid': vid, 'cu': cu, 'vd': vd})
    else:
        return redirect("/client/client_login")


def client_signup(request):
    ar = Area.objects.all()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/client/client")
            except:
                print("--------", sys.exc_info())
    else:
        form = CustomerForm()
    return render(request, "client_sign-up.html", {'form': form, 'ar': ar})


def client_login(request):
    if 'client_id' not in request.session:
        if request.method == "POST":
            email = request.POST["cust_email"]
            password = request.POST["password"]
            val = Customer.objects.filter(cust_email=email, password=password, is_admin=1).count()
            print("-------------------", email, "---------------------", password)
            if val == 1:
                udata = Customer.objects.filter(cust_email=email, password=password, is_admin=1)
                for item in udata:
                    request.session['client_email'] = item.cust_email
                    request.session['client_pass'] = item.password
                    request.session['client_id'] = item.cust_id
                    if request.POST.get("remember"):
                        response = redirect('/client/client/')
                        response.set_cookie('C_client_email', request.POST['cust_email'], 3600 * 24 * 365 * 2)
                        response.set_cookie('C_client_pass', request.POST['password'], 3600 * 24 * 365 * 2)
                        return response
                return redirect('/client/client/')
            else:
                messages.error(request, "Invalid Email or password")
                return redirect('/client/client_login/')
        else:
            if request.COOKIES.get("C_client_email"):
                return render(request, "client_login.html", {'client_email_cookie1': request.COOKIES['C_client_email'],
                                                             'client_password_cookie2': request.COOKIES[
                                                                 'C_client_pass']})
            else:
                return render(request, "client_login.html")
    else:
        return redirect("/client/client")


def client_logout(request):
    try:
        del request.session['client_email']
        del request.session['client_pass']
        del request.session['client_id']
    except:
        pass

    return redirect('/client/client_login')


from django.core.mail import send_mail
import random


def client_sendotp(request):
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
        print("**********", subject, "-*-*-*-", message, "-*-*-*-", email_from, "-*-*-*-", recipient_list,
              "***********")

        return render(request, 'client_set_password.html')


def client_forgot_password(request):
    if 'client_id' not in request.session:
        return render(request, "client_forgot.html")
    else:
        return redirect("/client/client")


def client_set_password(request):
    if 'client_id' not in request.session:
        if request.method == "POST":

            T_otp = request.POST['otp']
            T_pass = request.POST['password']
            T_cpass = request.POST['cpassword']

            if T_pass == T_cpass:

                e = request.session['temail']
                val = Customer.objects.filter(cust_email=e, otp=T_otp, otp_used=0).count()

                if val == 1:
                    Customer.objects.filter(cust_email=e).update(otp_used=1, password=T_pass)
                    return redirect("/client/client_login")
                else:
                    messages.error(request, "Invalid OTP")
                    return render(request, "client_forgot.html")

            else:
                messages.error(request, "New password and Confirm password does not match ")
                return render(request, "client_set_password.html")

        else:
            return redirect("/client/client_forpass")
    else:
        return redirect("/client/client")


def client_profile(request):
    if 'client_id' in request.session:
        id1 = request.session['client_id']
        cu = Customer.objects.get(cust_id=id1)
        ar = Area.objects.all()
        form = CustomerForm(request.POST, instance=cu)
        print("-----------***************---------", form.errors)
        if form.is_valid():
            print("*****************************")
            try:
                form.save()
                return redirect("/client/client_profile/")
            except:
                print("---------------", sys.exc_info())

        return render(request, "client_profile.html", {'cu': cu, 'ar': ar, 'id1': id1})
    else:
        return redirect("/client/client_login")


def client_feedback(request):
    if 'client_id' in request.session:
        fe = Feedback.objects.all()
        fcount = Feedback.objects.count()
        id1 = request.session['client_id']
        cu = Customer.objects.get(cust_id=id1)
        print("============================", id1)

        date = str(datetime.date.today())
        if request.method == "POST":
            form = FeedbackForm(request.POST)
            print("---------", form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("/client/client_feedback")
                except:
                    print("--------", sys.exc_info())
        else:
            form = FeedbackForm()
        return render(request, "client_feedback.html",
                      {'form': form, 'fe': fe, 'fcount': fcount, 'id1': id1, 'date': date, 'cu': cu})
    else:
        fe = Feedback.objects.all()
        fcount = Feedback.objects.count()
        return render(request, "client_feedback.html", {'fe': fe, 'fcount': fcount})


def client_about_us(request):
    if 'client_id' in request.session:
        id1 = request.session['client_id']
        cu = Customer.objects.get(cust_id=id1)
        return render(request, "client_about_us.html", {'cu': cu})
    else:
        return render(request, "client_about_us.html")


def client_contact(request):
    if 'client_id' in request.session:
        id1 = request.session['client_id']
        cu = Customer.objects.get(cust_id=id1)
        return render(request, "client_contact.html", {'cu': cu})
    else:
        return render(request, "client_contact.html")
