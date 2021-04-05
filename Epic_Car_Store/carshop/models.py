from django.db import models
from django.urls import reverse

# Create your models here.
class CarType(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60)

    type = models.ForeignKey(CarType, on_delete=models.DO_NOTHING, null=True, blank=True)
    year_released = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    manufacturer = models.CharField(max_length=60,null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={"id": self.id})
