from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def sendmail(request):
    subject = 'welcome'
    message = 'hello world!!!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ta5.sakshi.181130116002@gmail.com','rutvikshah979@gmail.com']
    send_mail(subject,message,email_from,recipient_list)
    return HttpResponse("mail sent..")