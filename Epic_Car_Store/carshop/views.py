from django.shortcuts import render
from django.http import HttpResponse



def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def free1(request, *args, **kwargs):
    return render(request, "free1.html", {})

def free2(request, *args, **kwargs):
    return render(request, "free2.html", {})

def free3(request, *args, **kwargs):
    return render(request, "free3.html", {})

def free4(request, *args, **kwargs):
    return render(request, "free4.html", {})




