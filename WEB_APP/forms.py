"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    sender = forms.EmailField()
    password = forms.CharField()
    host = forms.CharField()
    port = forms.IntegerField()
    subject = forms.CharField()
    recipient = forms.CharField()
    message = forms.CharField()
    attachment =forms.FileField(required=False)