from django.http import HttpResponseRedirect
import smtplib
from django.urls import reverse
from django.shortcuts import render
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
            text = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            password = form.cleaned_data["password"]
            recipients = form.cleaned_data['recipients']
            lists = recipients.split(',')
            '''
            message = f'Subject: {subject}\n\n{text}'
            '''
            message = "Subject:{}\n\n{}".format(subject,text)
            
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(sender, password)
                smtp.sendmail(sender, lists, message)
                return HttpResponseRedirect(reverse('home'))
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'WEB_APP/layout.html', {'form': form})
    