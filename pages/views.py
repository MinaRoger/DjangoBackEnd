from django.http import HttpResponse
from django.shortcuts import render


def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")


def about_view(*args, **kwargs):
    return HttpResponse("<h1>About Us</h1>")


def registration_view(request,*args, **kwargs):
    return render(request, "register.html", {})


def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})
