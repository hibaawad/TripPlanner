from django.db import models
from trip.models import Hotel, Restaurant, Attraction
# Create your models here.

class TripDetail(models.Model):
    user_id = models.CharField(max_length = 20)
    destination = models.CharField(max_length = 20)
    arrival = models.DateTimeField('arrival date')
    departure = models.DateTimeField('departure date')
    theme = models.CharField(max_length = 20)
    intensity = models.CharField(max_length = 10)
    cost = models.CharField(max_length = 10)
    hotel = models.ForeignKey(Hotel, null=True, blank=True, default = None)
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True, default = None)
    attraction = models.ForeignKey(Attraction, null=True, blank=True, default = None)


