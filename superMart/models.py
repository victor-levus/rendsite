from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.TextField(null=True, blank=True)
