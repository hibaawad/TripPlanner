# Create your views here.
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from trip.models import Hotel, Restaurant, Attraction
from django.db import models
from wizard.models import TripDetail;
from django.utils.safestring import mark_safe
from django import template
from django.shortcuts import render_to_response
import json
from datetime import datetime, date, time, timedelta
import random

def encodeAttraction(obj):

   d = {"id": obj.id,
        "name":  obj.name,
        "address" : obj.address,
        "latitude" :obj.latitude,
        "longitude" : obj.longitude,
        "googleReference" : obj.googleReference,
        "category": obj.category,
        "fun": obj.fun,
        "history": obj.history,
        "museum": obj.museum,
        "phoneNumber": obj.phoneNumber,
        "url": obj.url,
        "website": obj.website,
        "hours": obj.hours}
   return d

def encodeEvent(obj):
    d = {"title": obj.title,
            "start":  obj.start.strftime('%Y-%m-%d %H:%M:%S'),
            "end" : obj.end.strftime('%Y-%m-%d %H:%M:%S'),
            "editable" :obj.editable,
            "place" : encodeAttraction(obj.place),
            "allDay" : False
         }
    return d            


class Event(object):
    def __init__(self, title, start, end, place, editable = True):
        self.title = title
        self.start = start
        self.end = end
        self.editable = editable
        self.place = place

        
def results(request, city, days, theme, intensity, luxury):
    place = request.GET.has_key('type')
    print'place', place
    hotels = Hotel.objects.all();
    if place:
        order = request.GET['order']
        print 'order', order
        if order == 'a':
            hotels = Hotel.objects.order_by('price');
            for hotel in hotels:
                print hotel.price
        elif order == 'd':
            hotels = Hotel.objects.order_by('-price');
    
    t = loader.get_template('trip/results.html')
 
    restaurants = Restaurant.objects.all();
    attractions = Attraction.objects.all();
    now = datetime.now()
    tripDetail = TripDetail (destination = city, arrival = now,
                             departure = now, theme = theme, intensity = intensity,
                             cost = luxury)
    tripDetail.save()
    tripId = tripDetail.id     # Returns the ID of your new object.
    totalAttractions = int(days) * 8;
    #print 'days', days
    #print 'totalAttractions', totalAttractions
    tripAttractions = random.sample(attractions, totalAttractions)
    #print "length of tripAttractions", len(tripAttractions)
    schedule = []
    hotel = random.choice(hotels)
    date = datetime.strptime(request.session["date"], "%a, %d %b %Y %H:%M:%S %Z") 
 
    events = []
    #for each day 
    for day in range(int(days)):
        schedule.append([])
        schedule[day] = []
        #adjust day
        startTime = date + timedelta(days = day)
        time = startTime
        #attractions per day
        for index in range (day*8,day*8 + 8):
            print 'index', index
            attraction = tripAttractions[index]
            duration = random.randrange(60,120, 10)
            endtime = time + timedelta(minutes = duration)
            e = Event (title = attraction.name, start=time, end = endtime, place = attraction)
            interval = random.randrange(30,50, 10)
            time = endtime + timedelta(minutes = interval)
            events.append(e)
            schedule[day].append(e)

            
    c = Context({'city': city,
                 'days': days,
                 'theme':theme,
                 'intensity':intensity,
                 'hotels':hotels,
                 'hotel':hotel,
                 'restaurants': restaurants,
                 'attractions': attractions,
                 'tripId': tripId,
                 'start': date.strftime('%Y-%m-%dT%H:%M:%S'),
                 'schedule': json.dumps(schedule, default = encodeEvent),
                 'events': json.dumps(events, default = encodeEvent)
                 })

    return HttpResponse(t.render(c))

##def makeHtml(place):
##   
##    	<div class="accordion" id="hotelAccordion">
##								{% for hotel in hotels %}
##								<div class="accordion-group">
##              					<div class="accordion-heading">
##                				<a class="accordion-toggle" data-toggle="collapse" data-parent="hotelAccordion" href="#{{hotel.id}}" onclick = "showInfo({{hotel.id}})">
##                 				{{hotel.name}} <span class = stars>{{hotel.rating}}</span>
##                 				</a>
##              					</div>
##              					<div id="{{hotel.id}}" class="accordion-body collapse" style="height: 0px; ">
##                					<div class="accordion-inner">
##                					
##                						Phone Number: {{hotel.phoneNumber}}
##                						Address : {{hotel.address}}
##                						
##                						{% if hotel.website %}
##                							</br><a href = "{{hotel.website}}" >website</a>
##                						{% endif %}
##                						
##                						
##                						{% if hotel.url %}
##                							</br><a href = "{{hotel.url}}" >url</a>
##                						{% endif %}
##                				
##                						
##                							{% for review in hotel.review_set.all %}
##                							</p>
##                								{%for rating in review.rating_set.all %}
##                									</br> {{rating.aspect}} : {{rating.rating}} 
##                								{%endfor %}
##                							{{review.text}}
##                							</p>
##                							Name: {{review.author}}
##                							</p>
##                							Time {{review.time}}
##                							</p>
##                							{% endfor %}
##                						
##                						
##                						<a id="link{{hotel.id}}" href="/trip/hotel/{{ hotel.id }}/">More info</a> 
##                						
##                					</div>
##              					</div>
##            				</div>
##				
##								{% endfor %}
##						</div>

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
