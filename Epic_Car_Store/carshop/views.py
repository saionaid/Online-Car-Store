from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Product, CarType
from django.views.generic import ListView

class ProductListView(ListView):
    queryset = Product.objects.all()


    def product_list_view(request):
        products = Product.objects.all()
        context = {
            'object_list': products
        }
        return render(request, 'cars.html', context)






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
    return render(request, "cars.html", {})

def contact_form(request, *args, **kwargs):
    return render(request, "contact_form.html", {})

def free4(request, *args, **kwargs):
    return render(request, "free4.html", {})

def hydrogen(request, *args, **kwargs):
    return render(request, "Hydrogen.html", {})

def diesel(request, *args, **kwargs):
    return render(request, "Diesel.html", {})

def petrol(request, *args, **kwargs):
    return render(request, "Petrol.html", {})

def electric(request, *args, **kwargs):
    return render(request, "Electric.html", {})

def gas(request, *args, **kwargs):
    return render(request, "products/Gas.html", {})

def hybrid(request, *args, **kwargs):
    return render(request, "Hybrid.html", {})


