from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    latitude = models.FloatField()
    longitude = models.FloatField()
    googleReference = models.CharField (max_length = 70)
    
class Hotel(Place):
    price = models.CharField(max_length = 20)
    rating = models.IntegerField()
    subcategory_rating = models.IntegerField()
    phoneNumber = models.CharField(max_length = 10)
    url = models.URLField()
    website = models.URLField()

class Restaurant(Place):
    cuisine = models.CharField(max_length = 20)
    price = models.CharField(max_length = 20)
    theme = models.CharField(max_length = 20)
    rating = models.IntegerField()
    subcategory_rating = models.IntegerField()
    phoneNumber = models.CharField(max_length = 10)
    url = models.URLField(null = True)
    website = models.URLField(null = True)
    hours = models.CharField(max_length = 20)

class Attraction(Place):
    category = models.CharField(max_length = 20)
    fun = models.IntegerField()
    history = models.IntegerField()
    museum = models.IntegerField()
    phoneNumber = models.CharField(null = True, max_length = 10)
    url = models.URLField(null = True)
    website = models.URLField(null = True)
    hours = models.CharField(null = True, max_length = 20)

class Review(models.Model):
    author = models.CharField(max_length = 70)
    author_url = models.URLField(null = True)
    text = models.CharField(max_length = 20)
    place = models.ForeignKey(Place)
    time = models.DateTimeField("time")
    
class Rating (models.Model):
    aspect = models.CharField(max_length = 10)
    rating = models.IntegerField()
    review = models.ForeignKey(Review)
    

