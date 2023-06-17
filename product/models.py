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


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    photo = models.ImageField(upload_to="uploads", height_field=None, width_field=None, max_length=None)
     
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    number_of_product = models.PositiveSmallIntegerField(default=0)
    is_mini = models.BooleanField(default=True)
    # user_locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.name