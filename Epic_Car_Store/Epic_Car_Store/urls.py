"""Epic_Car_Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from carshop.views import homepage_view, cars, contact_form, login, free4
from carshop.views import register




urlpatterns = [
    path('', homepage_view),
    path("register/", register, name='register'),
    path('cars/',  cars),
    path('contact_form/', contact_form),
    path('Login/', login),
    path('free4/', free4),
    path('admin/', admin.site.urls),

]
