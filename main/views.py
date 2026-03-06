from django.shortcuts import render, reverse, redirect
from .models import StaffModel, GalaryModel, ContactModel, NewsModel, Customer, BannerModel
from . import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings


def about(request):  # SECTION --> ABOUT
    PointingContacting = ContactModel.objects.first()
    GalaryAnswer = GalaryModel.objects.all()
    PointingNews = NewsModel.objects.all()
    StaffAnswer = StaffModel.objects.all()
    BannerAnswer = BannerModel.objects.first()

    Input = {
        "AboutContact": PointingContacting,
        "Galary": GalaryAnswer,
        "News": PointingNews,
        "Staff": StaffAnswer,
        "Banner": BannerAnswer
    }

    return render(request, "index.html", Input)


def staff(request):  # SECTION --> STAFF
    PointingContacting = ContactModel.objects.first()
    BannerAnswer = BannerModel.objects.first()

    Input = {
        "AboutContact": PointingContacting,
        "Staff": StaffModel.objects.all(),
        "Banner": BannerAnswer
    }

    return render(request, "index-staff.html", Input)


def news(request):  # SECTION --> NEWS
    PointingContacting = ContactModel.objects.first()
    PointingNews = NewsModel.objects.all()
    BannerAnswer = BannerModel.objects.first()

    Input = {
        "AboutContact": PointingContacting,
        "News": PointingNews,
        "Banner": BannerAnswer
    }

    return render(request, "index-news.html", Input)


def galary(request):  # SECTION --> GALARY
    PointingContacting = ContactModel.objects.first()
    GalaryAnswer = GalaryModel.objects.all()
    BannerAnswer = BannerModel.objects.first()

    Input = {
        "AboutContact": PointingContacting,
        "Galary": GalaryAnswer,
        "Banner": BannerAnswer
    }

    return render(request, "index-galary.html", Input)


def contact(request):  # SECTION --> CONTACT
    Submit = False
    PhoneError = False
    PointingContacting = ContactModel.objects.first()
    BannerAnswer = BannerModel.objects.first()

    if request.method == 'POST':
        form = forms.InputForm(request.POST)

        if form.is_valid():  # IF IT IS VALID
            phone = form.cleaned_data['phone_number']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            CustomerInput = Customer(name=name, phone_number=phone, message=message)
            CustomerInput.save()

            '''
            smtp = smtplib.SMTP() # we should import smtplib for working it
            smtp.connect(settings.EMAIL_HOST, 25)
            smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            smtp.sendmail(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER, message, as_string())
            smtp.quit()
            '''

            subject = f"Message from {name} and {phone}"
            message_to_user = f"{message}"
            host = settings.EMAIL_HOST_USER
            To = [settings.EMAIL_HOST_USER]
            # DON'T SHOW THE ERROR ON SENDING MESSAGE TO EMAIL IF THE EMAIL PASSWORD IS INVALID! (Fixed BUG crash)
            send_mail(subject, message_to_user, host, To, True)  # False when email is failed!

            # send_main(String Subject, String Message, String FromEmail, [String ToEmail], boolean NotShowAnError)
            return HttpResponseRedirect("?submitted=Valid")  # ?submitted=Valid&Check=True
        else:  # IF NOT VALID IN CASE WHEN USER FAILS IN SOMEWHERE!
            error_result = f"?Errors{'=PhoneError' if bool(form['phone_number'].errors) is True else '=Invalid'}"
            return HttpResponseRedirect(error_result)

    if request.GET.get("submitted") == "Valid":
        Submit = True

    elif request.GET.get("Errors") == "PhoneError":
        PhoneError = True

    Input = {
        "Is_Send": Submit,
        "Is_Phone_Error": PhoneError,
        "AboutContact": PointingContacting,
        "Banner": BannerAnswer
    }
    return render(request, "index-contact.html", Input)
