from django.db import models
import os
import time
from users.models import User as BotUser

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
    photo = models.ImageField(upload_to="uploads", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    price = models.IntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children", null=True, blank=True)

    # number_of_product = models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return self.name

class Basket(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    count = models.PositiveSmallIntegerField(default=0)
    price = models.PositiveSmallIntegerField(default=0)
