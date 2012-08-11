from django.conf.urls import patterns, include, url
from django.views.generic import DetailView

from wizard.models import Hotel, Attraction, Restaurant
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'travelsite.views.home', name='home'),
    # url(r'^travelsite/', include('travelsite.foo.urls')),
    url (r'^wizard/', include ('wizard.urls')),
    url (r'^trip/hotel/(?P<pk>\d+)/$', DetailView.as_view( model = Hotel, template_name = '/trip/hotel_detail.html')),
    url (r'^trip/attraction/(?P<pk>\d+)/$', DetailView.as_view( model = Attraction, template_name = 'trip/attraction_detail.html')),
    url (r'^trip/restaurant/(?P<pk>\d+)/$', DetailView.as_view( model = Restaurant, template_name = 'trip/restaurant_detail.html')),
    url (r'^trip/(?P<tripId>\d+)/hotel/(?P<hotelId>\d+)/add/$', 'trip.views.addHotel'),
    url (r'^trip/(?P<city>\w+)/(?P<days>\w+)/(?P<theme>\w+)/(?P<intensity>\w+)/(?P<luxury>\w+)/$', 'trip.views.results'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
