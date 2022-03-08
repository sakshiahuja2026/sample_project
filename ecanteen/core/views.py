from re import template
from django.shortcuts import render
from django.contrib.auth.views import LoginView
# Create your views here.
class UserLogin(LoginView):
    template_name='core/login.html'
    success_url="/admin"

#class UserLogout(LogoutView):
    #pass
    #template_name='core/logout.html'
    