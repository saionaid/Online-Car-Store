from django.shortcuts import render
from django.http import HttpResponse



def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def cars(request, *args, **kwargs):
    return render(request, "cars.html", {})

def contact_form(request, *args, **kwargs):
    return render(request, "contact_form.html", {})

def login(request, *args, **kwargs):
    return render(request, "Login.html", {})

def free4(request, *args, **kwargs):
    return render(request, "free4.html", {})




