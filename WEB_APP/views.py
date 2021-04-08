"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import ContactForm
from django.http import HttpResponseRedirect
import smtplib, ssl
from django.urls import reverse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from .models import files
from django.core.files.storage import FileSystemStorage
import os, os.path
import imghdr
from django.conf import settings
from email.message import EmailMessage

document = files()


def smtp(request):
    if request.method == 'POST':
        
        subject = request.POST['subject']
        text = request.POST['message']
        sender = request.POST['sender']
        password = request.POST["password"]
        host = request.POST['host']
        port = request.POST['port']
        cc = request.POST['cc']
        document.attachment == request.FILES['attachment']
        recipient = request.POST['recipient']
        lists = recipient.split(',')
        
        document.save()


        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = lists
        msg.set_content(text)
        
        print(document)
        save_files = settings.MEDIA_ROOT
        with open(save_files + f'{document}', 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
            print(file_type)

        msg.add_attachment(file_data, filename=file_name, maintype=file_type, subtype=file_type)
            
        with smtplib.SMTP_SSL(f'{host}', port) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
            smtp.quit()
            return render(request, "WEB_APP/layout.html",{'message': "Mail Sent!"})
       
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'WEB_APP/layout.html', {
        'year':datetime.now().year,
        })
    return render(request, "WEB_APP/layout.html",{'message': "Mail Sent!"})
    