from django.forms import Form, ModelForm
from . import models
from django import forms
from django.contrib import admin
import regex
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect


def checker_of_phone_number(phone_number):
    result = regex.match("^\+(998)[0-9]{9}$", phone_number)
    result = bool(result)  # well we convert our regex expression to boolean then it will return us true or false!

    if result is False:
        raise ValidationError("Kiritayotgan telefon raqamingiz tasdiqlinashiga yaroqsiz!")


class InputForm(forms.Form):  # We could use Form too but for now I am learning ModelForm which is connected to models
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Habaringizni kiriting"}),
                              max_length=1500, required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ismingizni kiriting"}),
                           max_length=120, required=True)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Telefon raqamingizni kiriting"}),
                                   max_length=13, required=True, validators=[checker_of_phone_number])

    '''
        class Meta:
        model = models.Customer
        fields = ["phone_number", "name", "message"]
        exclude = ["created_at"]
    '''
