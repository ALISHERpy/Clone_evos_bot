from django.db import models

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

    photo = models.FileField(upload_to=None, max_length=100)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    number_of_product = models.PositiveSmallIntegerField(default=0)
    is_mini = models.BooleanField(default=True)
    # user_locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.name