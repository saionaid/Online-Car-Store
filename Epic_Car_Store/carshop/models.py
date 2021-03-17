from django.db import models

# Create your models here.

class Type_of_the_Car(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name


class Car_2(models.Model):
    name = models.CharField(max_length=60)
    type = models.ForeignKey(Type_of_the_Car, on_delete=models.DO_NOTHING, null=True, blank=True)
    year_released = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    in_stock = models.BooleanField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return self.name + '-' + str(self.id)
