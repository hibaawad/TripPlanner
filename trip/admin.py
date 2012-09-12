from trip.models import *
from django.contrib import admin

#admin.site.register(Hotel)
admin.site.register(Restaurant)
admin.site.register(Attraction)
#admin.site.register(Review)
#admin.site.register(Rating)

class RegisterInline (admin.StackedInline):
    model = Rating
    extra = 5
    
class ReviewInline(admin.StackedInline):
    model = Review
    extra = 5


class ReviewAdmin (admin.ModelAdmin):
    inlines = [RegisterInline]
    
class HotelAdmin(admin.ModelAdmin):
   
    inlines = [ReviewInline]

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Review, ReviewAdmin)
