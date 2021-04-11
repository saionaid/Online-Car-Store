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
from django.urls import path, include
from carshop.views import *
from carshop.views import register




urlpatterns = [
    path('home/', homepage_view, name="home"),
    path("register/", register, name='register'),
    path('cars/',  cars, name="cars"),
    path("contact_form/", contact, name="contact"),
    path('free4/', free4),
    path('product_detail/', CarDetailView.as_view(), name='productdetail'),
    path('carslist/', CarsListView.as_view(), name='carslist'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_detail/<int:pk>/', CarDetailView.as_view(), name='Detailcar'),
    path('admin/', admin.site.urls),
    path('product_list/<int:pk>', ProductListView.as_view(), name='list_of_cars'),
    path('product_create/', ProductCreateView.as_view(), name='createnew'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('Congrats/', congrats, name='Congrats'),
    path('', include("django.contrib.auth.urls")),
]
