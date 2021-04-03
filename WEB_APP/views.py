from django.http import HttpResponseRedirect
import smtplib
from django.urls import reverse
from django.shortcuts import render
import imghdr
from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField()
    password = forms.CharField()
    host = forms.CharField()
    port = forms.IntegerField()
    subject = forms.CharField()
    recipient = forms.CharField()
    message = forms.CharField()
'''
class ContactForm(forms.Form):
    sender = forms.EmailField(label='Sender', widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))
    host = forms.CharField(label='Host', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    port = forms.IntegerField()
    subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    recipients = forms.CharField(label='Recipients', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    message = forms.CharField(label='Message',  widget=forms.Textarea(attrs={'class': 'form-control'}))
'''

def home(request):
    return render(request, "WEB_APP/success.html")

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = ContactForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
        subject = request.POST['subject']
        text = request.POST['message']
        sender = request.POST['sender']
        password = request.POST["password"]
        host = request.POST['host']
        print(host)
        port = request.POST['port']
        print(port)
        recipient = request.POST['recipient']
        lists = recipient.split(',')
        '''
        message = f'Subject: {subject}\n\n{text}'
        '''
        message = "Subject:{}\n\n{}".format(subject,text)
            
        with smtplib.SMTP_SSL(f'{host}', port) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, lists, message)
            smtp.quit()
            return render(request, "WEB_APP/layout.html",{'message': "Mail Sent!"})
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'WEB_APP/layout.html', {'form': form})
    