from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, request
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.template import Context, loader
from django.contrib.auth.models import User
from .forms import UserForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        user.set_password(password)
        user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'webportal/homepage.html')
    context = {
        "form": form,
    }
    return render(request, 'webportal/registration.html', context)

def termsandcondition(request):
    template = loader.get_template("webportal/termsandcondition.html")
    return HttpResponse(template.render())


def index(request):
    template = loader.get_template("webportal/index.html")
    return HttpResponse(template.render())


def LoginForm(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return render(request, 'webportal/homepage.html')
            else:
                return render(request, 'webportal/login.html', {'error_message': 'Your account has been disabled.'})
        else:
            return render(request, 'webportal/login.html', {'error_message':'Invalid Login'})
    else:
        return render(request, 'webportal/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'webportal/login.html', context)


def homepage(request):
    template = loader.get_template("webportal/homepage.html")
    return HttpResponse(template.render())
