import datetime
import sys

from django.shortcuts import render, redirect

from movepack import settings
from ssr.forms import *
from ssr.models import *
from django.contrib import messages


# Create your views here.

def show(request):
    print("*************************")
    id1 = request.session['driver_id']
    dr = Driver.objects.get(dri_id=id1)
    return render(request, "driver_header.html")


def driver_index(request):
    if 'driver_id' in request.session:
        id1 = request.session['driver_id']
        dr = Driver.objects.get(dri_id=id1)
        bo = Booking.objects.filter(dri_id=id1)
        date = datetime.date.today()
        if request.method == "POST":

            dri = request.POST.get('is_available')
            print("==============================================", dri)
            if dri == '0':
                print("---------inside if----")
                dr.is_available = 0
                dr.save()
            elif dri == '2':
                print("---------inside else----")
                dr.is_available = 2
                dr.save()
        return render(request, "driver_index.html", {'dr': dr, 'bo': bo, 'date': date})
    else:
        return redirect("/driver/driver_login")


def driver_register(request):
    if 'driver_id' not in request.session:
        if request.method == "POST":
            form = DriverForm(request.POST)
            print("---------", form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("/driver/driver")
                except:
                    print("--------", sys.exc_info())
        else:
            form = DriverForm()
        return render(request, "driver_register.html", {'from': form})
    else:
        return redirect("/driver/driver")


def driver_login(request):
    if 'driver_id' not in request.session:
        if request.method == "POST":
            email = request.POST["dri_email"]
            password = request.POST["password"]
            val = Driver.objects.filter(dri_email=email, password=password).count()
            print("-------------------", email, "---------------------", password, "========", val)
            if val == 1:
                udata = Driver.objects.filter(dri_email=email, password=password)
                for item in udata:
                    request.session['driver_email'] = item.dri_email
                    request.session['driver_pass'] = item.password
                    request.session['driver_id'] = item.dri_id
                    if request.POST.get("remember"):
                        response = redirect('/driver/driver/')
                        response.set_cookie('D_driver_email', request.POST['dri_email'], 3600 * 24 * 365 * 2)
                        response.set_cookie('D_driver_pass', request.POST['password'], 3600 * 24 * 365 * 2)
                        return response
                return redirect('/driver/driver/')
            else:
                messages.error(request, "Invalid Email or password")
                return redirect('/driver/driver_login/')
        else:
            if request.COOKIES.get("D_driver_email"):
                return render(request, "driver_login.html", {'driver_email_cookie1': request.COOKIES['D_driver_email'],
                                                             'driver_password_cookie2': request.COOKIES['D_driver_pass']})
            else:
                return render(request, "driver_login.html")
    else:
        return redirect("/driver/driver")


def driver_logout(request):
    try:
        del request.session['driver_email']
        del request.session['driver_pass']
        del request.session['driver_id']
    except:
        pass

    return redirect('/driver/driver_login')


from django.core.mail import send_mail
import random


def driver_sendotp(request):
    otp1 = random.randint(10000, 99999)
    e = request.POST['email']

    request.session['temail'] = e

    obj = Driver.objects.filter(dri_email=e).count()

    if obj == 1:
        val = Driver.objects.filter(dri_email=e).update(otp=otp1, otp_used=0)

        subject = 'OTP Verification'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)
        print("**********", subject, "-*-*-*-", message, "-*-*-*-", email_from, "-*-*-*-", recipient_list,
              "***********")

        return render(request, 'driver_set_password.html')


def driver_forgot_password(request):
    if 'driver_id' not in request.session:
        return render(request, "driver_forgot.html")
    else:
        return redirect("/driver/driver")


def driver_set_password(request):
    if 'driver_id' not in request.session:
        if request.method == "POST":

            T_otp = request.POST['otp']
            T_pass = request.POST['password']
            T_cpass = request.POST['cpassword']

            if T_pass == T_cpass:

                e = request.session['temail']
                val = Driver.objects.filter(dri_email=e, otp=T_otp, otp_used=0).count()

                if val == 1:
                    Driver.objects.filter(dri_email=e).update(otp_used=1, password=T_pass)
                    return redirect("/driver/driver_login")
                else:
                    messages.error(request, "Invalid OTP")
                    return render(request, "driver_forgot.html")

            else:
                messages.error(request, "New password and Confirm password does not match ")
                return render(request, "driver_set_password.html")

        else:
            return redirect("/driver/driver_forpass")
    else:
        return redirect("/driver/driver")


def driver_profile(request):
    if 'driver_id' in request.session:
        id1 = request.session['driver_id']
        dr = Driver.objects.get(dri_id=id1)
        return render(request, "driver_profile.html", {'dr': dr, 'id1': id1})
    else:
        return redirect("/driver/driver_login")


def driver_edit_profile(request):
    if 'driver_id' in request.session:
        id1 = request.session['driver_id']
        dr = Driver.objects.get(dri_id=id1)

        form = DriverForm(request.POST, instance=dr)
        print("-----------***************---------", form.errors)
        if form.is_valid():
            print("*****************************")
            try:
                form.save()
                return redirect("/driver/driver_profile/")
            except:
                print("---------------", sys.exc_info())

        return render(request, "driver_edit_profile.html", {'dr': dr, 'id1': id1})
    else:
        return redirect("/driver/driver_login")


def driver_booking_complete(request, id):
    if request.method == "POST":
        vf = request.POST.get("verification")
        b = Booking.objects.get(book_id=id)

        if b.payment_type == 1 and b.payment_status == 1:

            if b.otp == vf:
                b.booking = '3'
                b.save()

                id1 = request.session['driver_id']
                dr = Driver.objects.get(dri_id=id1)
                dr.is_available = '0'
                dr.save()
                return redirect("/driver/driver")
            else:
                messages.error(request, "Invalid OTP")
                print("*-*-*-* Wrong OTP *-*-*-*", vf)
                return redirect("/driver/driver")

        elif b.payment_type == 2:

            if b.otp == vf:
                b.booking = '3'
                b.payment_status = '1'
                b.save()

                id1 = request.session['driver_id']
                dr = Driver.objects.get(dri_id=id1)
                dr.is_available = '0'
                dr.save()
                return redirect("/driver/driver")
            else:
                messages.error(request, "Invalid OTP")
                print("*-*-*-* Wrong OTP *-*-*-*", vf)
                return redirect("/driver/driver")

        else:
            messages.error(request, "Payment Pending")
            print("*-*-*-* Wrong OTP *-*-*-*", vf)
            return redirect("/driver/driver")

    else:
        print("======== request.method Error is occur ========")
        return redirect("/driver/driver")


def driver_bookings(request):
    if 'driver_id' in request.session:
        id1 = request.session['driver_id']
        dr = Driver.objects.get(dri_id=id1)
        bo = Booking.objects.filter(dri_id=id1).order_by('-book_id')
        date = datetime.date.today()
        return render(request, "driver_bookings.html", {'dr': dr, 'bo': bo, 'date': date})
    else:
        return redirect("/driver/driver_login")


# def is_available(request):
#     if 'driver_id' in request.session:
#         id1 = request.session['driver_id']
#         dr = Driver.objects.get(dri_id=id1)
#         dri = request.POST.get('is_available')
#         if dri == 0:
#             dr.is_available = 0
#             dr.save()
#         elif dri == 2:
#             dr.is_available = 2
#             dr.save()
#         return render(request, "driver_index.html", {'dr': dr})
#     else:
#         return redirect("/driver/driver_login")
