from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=30)
    year_released = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    manufacturer = models.CharField(max_length=60,null=True)

    def __str__(self):
        return self.name + '-' + str(self.id)
