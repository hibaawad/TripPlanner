from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length = 20)
    price = models.CharField(max_length = 20)
    rating = models.CharField(max_length = 20)
    subcategory_rating = models.CharField(max_length = 20)


class Restaurant(models.Model):
    name = models.CharField(max_length= 20)
    address = models.CharField(max_length = 20)
    cuisine = models.CharField(max_length = 20)
    price = models.CharField(max_length = 20)
    rating = models.CharField(max_length = 20)
    subcategory_rating = models.CharField(max_length = 20)


class Attraction(models.Model):
    name = models.CharField(max_length= 20)
    address = models.CharField(max_length = 20)
    category = models.CharField(max_length = 20)
    fun = models.CharField(max_length = 20)
    museum = models.CharField(max_length = 20)
