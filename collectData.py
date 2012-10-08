import urllib2
import urllib
import json
import datetime
from trip.models import *

def fixCarriageReturns(inputFile, outputFile):

    w = open(outputFile, 'r+')
    f = open(inputFile)
    for line in f:
        print line
        line2 = line.replace("\r","\n")
        print line
        w.write(line2)
   

def saveHotelDetails(filename, placeType):
    f = open(filename)
      
    for line in f:
        information = line.split(',')
        print information
        name = information [0]
        #compose a URL to call geocode API
        #print 'trying to make a connection'

        result = searchQuery(name, placeType)
        if (result == None):
            print 'could not load results for following name :', name
        else:
            latitude, longitude, reference, name= result

            json_data = detailsQuery(reference)

            address = json_data["result"]["formatted_address"]
            phoneNumber = json_data["result"]["formatted_phone_number"]
            if "rating" in json_data["result"]:
                rating=json_data["result"]["rating"]
            else:
                rating = information[2]
         
            url = json_data["result"]["url"]
            website = json_data["result"]["website"]
            
            hotel = Hotel(name = name, address = address, latitude = latitude, phoneNumber = phoneNumber,
                          longitude = longitude, googleReference = reference, price = information[2], rating = rating,
                          subcategory_rating = information[4], url = url, website = website)
            hotel.save()

            if "reviews" in json_data["result"]:
                
                reviews=json_data["result"]["reviews"] 
                for rev in reviews:
                    author = rev["author_name"]
                    if "author_url" in rev:
                        author_url = rev["author_url"]
                    else:
                        author_url = None
                    text = rev["text"]
                    dt = datetime.datetime.fromtimestamp(rev["time"]/1000.0)
                    r = Review(author = author, author_url =author_url, text = text, time = dt, place = hotel)
                    r.save()
         
                    for aspect in rev["aspects"]:
                        rating_type = aspect["type"]
                        value = aspect["rating"]
                        rating = Rating(aspect = rating_type, rating = value, review = r)
                        rating.save();
                
def saveAttractionDetails(filename, placeType):
    f = open(filename)
      
    for line in f:
        information = line.split(',')
        print information
        name = information [0]
        #compose a URL to call geocode API
        #print 'trying to make a connection'

        result = searchQuery(name, placeType)
        if (result == None):
            print 'could not load results for following name :', name
        else:
            latitude, longitude, reference, name= result

            json_data = detailsQuery(reference)

            address = json_data["result"]["formatted_address"]
            if "formatted_phone_number" in json_data["result"]:
                phoneNumber = json_data["result"]["formatted_phone_number"]
            else:
                phoneNumber = None
            if "rating" in json_data["result"]:
                rating=json_data["result"]["rating"]
            else:
                rating = None
         
            if "url" in json_data["result"]:
                url = json_data["result"]["url"]
            else:
                url = None
            
            if "website" in json_data["result"]:
                website = json_data["result"]["website"]
            else:
                website = None

            hours = ""
            if "opening_hours" in json_data["result"]:
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                for period in json_data["result"]["opening_hours"]["periods"]:
                    index = period["open"]["day"] -1
                    day = days[index]
                    timeOpen = period["open"]["time"]
                    timeClose = period["close"]["time"]
                    hours += day + ": "  + timeOpen + " - " + timeClose + " \n"
                    
            attraction = Attraction(name = name, address = address, latitude = latitude, longitude = longitude, phoneNumber = phoneNumber,
                        googleReference = reference, category = information[2], fun = information[3],
                        history = information[4], museum = information [5], url = url, website = website, hours = hours)
            attraction.save()

            if "reviews" in json_data["result"]:
                
                reviews=json_data["result"]["reviews"] 
                for rev in reviews:
                    author = rev["author_name"]
                    if "author_url" in rev:
                        author_url = rev["author_url"]
                    else:
                        author_url = None
                    text = rev["text"]
                    dt = datetime.datetime.fromtimestamp(rev["time"]/1000.0)
                    r = Review(author = author, author_url =author_url, text = text, time = dt, place = attraction)
                    r.save()
         
                    for aspect in rev["aspects"]:
                        rating_type = aspect["type"]
                        value = aspect["rating"]
                        rating = Rating(aspect = rating_type, rating = value, review = r)
                        rating.save();

def saveRestaurantDetails(filename, placeType):
    f = open(filename)
      
    for line in f:
        information = line.split(',')
        print information
        name = information [0]
        #compose a URL to call geocode API
        #print 'trying to make a connection'

        result = searchQuery(name, placeType)
        if (result == None):
            print 'could not load results for following name :', name
        else:
            latitude, longitude, reference, name= result

            json_data = detailsQuery(reference)

            address = json_data["result"]["formatted_address"]
            if "formatted_phone_number" in json_data["result"]:
                phoneNumber = json_data["result"]["formatted_phone_number"]
            else:
                phoneNumber = None
            if "rating" in json_data["result"]:
                rating=json_data["result"]["rating"]
            else:
                rating = information[4]
         
            if "url" in json_data["result"]:
                url = json_data["result"]["url"]
            else:
                url = None
            
            if "website" in json_data["result"]:
                website = json_data["result"]["website"]
            else:
                website = None

            hours = ""
            if "opening_hours" in json_data["result"]:
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                for period in json_data["result"]["opening_hours"]["periods"]:
                    index = period["open"]["day"] -1
                    day = days[index]
                    timeOpen = period["open"]["time"]
                    timeClose = period["close"]["time"]
                    hours += day + ": "  + timeOpen + " - " + timeClose + " \n"
            cuisine = information[2]
            budget = information[3]
            subcategory = information[5]
            theme = information[6]
            
            restaurant = Restaurant(name = name, address = address, latitude = latitude, longitude = longitude, phoneNumber = phoneNumber,
                        googleReference = reference, cuisine = cuisine, price = budget, subcategory_rating = subcategory,
                        theme = theme, url = url, website = website, hours = hours, rating = rating)
            restaurant.save()

            if "reviews" in json_data["result"]:
                
                reviews=json_data["result"]["reviews"] 
                for rev in reviews:
                    author = rev["author_name"]
                    if "author_url" in rev:
                        author_url = rev["author_url"]
                    else:
                        author_url = None
                    text = rev["text"]
                    dt = datetime.datetime.fromtimestamp(rev["time"]/1000.0)
                    r = Review(author = author, author_url =author_url, text = text, time = dt, place = restaurant)
                    r.save()
         
                    for aspect in rev["aspects"]:
                        rating_type = aspect["type"]
                        value = aspect["rating"]
                        rating = Rating(aspect = rating_type, rating = value, review = r)
                        rating.save();

def detailsQuery(reference):
 
     # Set the Places API key for your application
    AUTH_KEY = 'AIzaSyBoaE_uGohIbX5PVa5xs3iCxFq2JOS3tGk'

    # Define the location coordinates
    LOCATION = '42.3584308,-71.098326'

    QUERY = urllib.quote(reference)
    url =  ('https://maps.googleapis.com/maps/api/place/details/json?reference=%s&sensor=false&key=%s') % (QUERY, AUTH_KEY)
    print url
    # Send the GET request to the Geocode details service (using url from above)
    response = urllib2.urlopen(url)

    # Get the response and use the JSON library to decode the JSON
    json_raw = response.read()
    json_data = json.loads(json_raw)

    return json_data
   
def searchQuery ( name, placeType):
    
    # Set the Places API key for your application
    AUTH_KEY = 'AIzaSyBoaE_uGohIbX5PVa5xs3iCxFq2JOS3tGk'

    # Define the location coordinates
    LOCATION = '42.3584308,-71.098326'

    # Define the radius (in meters) for the search
    RADIUS = 5000
    
    QUERY = urllib.quote(name)
    url =  ('https://maps.googleapis.com/maps/api/place/search/json?location=%s&radius=10000&types=%s&name=%s&sensor=false&key=%s') % (LOCATION,placeType, QUERY, AUTH_KEY)
    print url
    
    # Send the GET request to the Geocode details service (using url from above)
    response = urllib2.urlopen(url)

    # Get the response and use the JSON library to decode the JSON
    json_raw = response.read()
    json_data = json.loads(json_raw)

    if json_data["status"] == 'OK':
        latitude = json_data["results"][0]["geometry"]["location"]["lat"]
        longitude = json_data["results"][0]["geometry"]["location"]["lng"]
        reference = json_data["results"][0]["reference"]
        name = json_data["results"][0]["name"]
        return latitude, longitude, reference, name
    
 
def printStuff1():
    print 'blah'

if __name__ == "__main__":
    
    fixCarriageReturns("restaurants.csv", "restaurants1.csv")

    
    #saveHotelDetails("hotels1.csv", "lodging")
