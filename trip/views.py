# Create your views here.
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from trip.models import Hotel, Restaurant, Attraction
from wizard.models import TripDetail;
import datetime



def results(request, city, days, theme, intensity, luxury):
    
    t = loader.get_template('trip/results.html')
    hotels = Hotel.objects.all();
    restaurants = Restaurant.objects.all();
    attractions = Attraction.objects.all();
    now = datetime.datetime.now()
    tripDetail = TripDetail (destination = city, arrival = now,
                             departure = now, theme = theme, intensity = intensity,
                             cost = luxury)
    tripDetail.save()
    tripId = tripDetail.id     # Returns the ID of your new object.
    c = Context({'city': city,
                 'days': days,
                 'theme':theme,
                 'intensity':intensity,
                 'hotels':hotels,
                 'restaurants': restaurants,
                 'attractions': attractions,
                 'tripId': tripId, 
                 })

    return HttpResponse(t.render(c))

def addHotel(request, tripId, hotelId):
    trip = TripDetail.objects.get(id = tripId)
    hotel = Hotel.objects.get(id = hotelId)
    trip.hotel = hotel
    trip.save()
    hotels = Hotel.objects.all();
    restaurants = Restaurant.objects.all();
    attractions = Attraction.objects.all();
    now = datetime.datetime.now()
    return render_to_response('trip/results.html', {
                 'hotels':hotels,
                 'restaurants': restaurants,
                 'attractions': attractions,
                 'tripId': trip.id, 
        }, context_instance=RequestContext(request))
