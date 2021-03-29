from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Product, CarType

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

            return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})


def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def cars(request,*args,**kwargs):
    product = Product.objects.all()
    return render(request, "cars.html", {})

def contact_form(request, *args, **kwargs):
    return render(request, "contact_form.html", {})

def login(request, *args, **kwargs):
    return render(request, "Login.html", {})

def free4(request, *args, **kwargs):
    return render(request, "free4.html", {})




