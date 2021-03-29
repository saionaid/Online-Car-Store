from django.contrib import admin

# Register your models here.

from .models import Product, CarType

admin.site.register(CarType)
admin.site.register(Product)