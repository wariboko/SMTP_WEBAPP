"""
Definition of views.
"""
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import ContactForm
from django.http import HttpResponseRedirect
import smtplib, ssl
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from django.core.files.storage import FileSystemStorage
import os, os.path
import imghdr
from django.conf import settings
from email.message import EmailMessage
from .models import User
from django.utils.datastructures import MultiValueDictKeyError

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("smtp"))
        else:
            return render(request, "WEB_APP/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "WEB_APP/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "WEB_APP/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "WEB_APP/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("smtp"))
    else:
        return render(request, "WEB_APP/register.html")

@login_required(login_url='accounts/login/')
def smtp(request):
    if request.method == 'POST':
        
        subject = request.POST['subject']
        text = request.POST['message']
        sender = request.POST['sender']
        password = request.POST["password"]
        host = request.POST['host']
        port = request.POST['port']
        
        recipient = request.POST['recipient']
        lists = recipient.split(',')
        
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = lists
        msg.set_content(text)
        try:
            document = request.FILES['attachment']
            documentByts = request.FILES['attachment'].read() 
        
            extension = document.name.split(".")[1]
            print(extension)
            
            msg.add_attachment(documentByts, filename=document.name, maintype=extension, subtype=extension)
        except MultiValueDictKeyError:
            document = False
        
        with smtplib.SMTP_SSL(f'{host}', port) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
            smtp.quit()
            return render(request, "WEB_APP/smtp.html",{'message': "Mail Sent!"})
       
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'WEB_APP/smtp.html', {
        'year':datetime.now().year,
        'date': datetime.now()
        })
    return render(request, "WEB_APP/smtp.html",{'message': "Mail Sent!"})
    