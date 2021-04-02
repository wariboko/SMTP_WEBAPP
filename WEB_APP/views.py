from django.http import HttpResponseRedirect
import smtplib
from django.urls import reverse
from django.shortcuts import render
from email.message import EmailMessage
import imghdr
from .forms import ContactForm

def home(request):
    return render(request, "WEB_APP/success.html")

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            password = form.cleaned_data["password"]
            recipients = form.cleaned_data['recipients']
            li = recipients.split(',')

            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = recipients
            msg.set_content(message)

            with open('/mnt/c/Users/40756/Onedrive/Documents/SMTP_APP/Cover Letter-David Wariboko.docx','rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                print(file_type)
                file_name = f.name
                print(file_name)
            msg.add_attachment(file_data, maintype='docx', subtype=file_type, filename=file_name)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(sender, password)
                smtp.send_message(msg)
                return HttpResponseRedirect(reverse('home'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'WEB_APP/layout.html', {'form': form})