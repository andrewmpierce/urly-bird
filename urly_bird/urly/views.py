from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
def loggedin(request):
    return render_to_response('registration/loggedin.html',
                              {'username': request.user.username})

class HomePage(TemplateView):
    template_name = 'home.html'

class LoginPage(TemplateView):
    template_name = 'urly/login.html'

class RegisterPage(TemplateView):
    template_name = 'urly/register.html'
