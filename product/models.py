from django.db import models
import os
import time

class Category(models.Model):
    name = models.CharField(max_length=64)
    photo = models.CharField(max_length=128, null=True, blank=True)


    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    photo = models.ImageField(upload_to="uploads", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # Variant 1
    variant1_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    variant1_description = models.CharField(max_length=256, null=True, blank=True)
    variant1_photo = models.ImageField(upload_to="uploads", null=True, blank=True)
    
    # Variant 2
    variant2_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    variant2_description = models.CharField(max_length=256, null=True, blank=True)
    variant2_photo = models.ImageField(upload_to="uploads", null=True, blank=True)
    
    def __str__(self):
        return self.name
