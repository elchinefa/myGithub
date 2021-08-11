from django.contrib import admin

from . models import Flight , Airport, Passenger

#modife admin page
class FlightAdmin(admin.ModelAdmin):
	list_display = ("id", "origin", "destination", "duration")


class PassengerAdmin(admin.ModelAdmin):
	filter_horizontal = ("flights",)

# Register your models here.
#let say django admin app that we want manupulate Airport and Flight in it
admin.site.register(Airport)
#admin.site.register(Flight) #after creating FlightAdmin class we changed it to:
admin.site.register(Flight, FlightAdmin)
#admin.site.register(Passenger) # #after creating PassengerAdmin class we changed it to:
admin.site.register(Passenger, PassengerAdmin)