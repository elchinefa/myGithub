from django.shortcuts import render
from .models import Flight, Passenger
from django.http  import HttpResponseRedirect
from django.urls import reverse

# After editin models.py I started add views.
def index(request):
	return render(request, "flights/index.html", {
		"flights": Flight.objects.all()
		})

def flight(request, flight_id):
	flight = Flight.objects.get(pk=flight_id) #get returns one result if not exists then gives error. We used here privat key (pk) but can also use get(id=flight_id)
	return render(request, "flights/flight.html", {
		"flight" : flight,
		"passengers": flight.passengers.all(), #passengers is related name which allows us to access all passengers on that flight
		"non_passengers": Passenger.objects.exclude(flights=flight).all()   #exclude all passenger on this fight and find non_passenger

		})  

def book(request, flight_id):
	if request.method == "POST":
		flight = Flight.objects.get(pk=flight_id)
		passenger = Passenger.objects.get(pk=int(request.POST["passenger"])) #because in form in  flight.html file we call <select name="passenger"> 	
		passenger.flights.add(flight) # will add new passenger for that flibg in to database table
		return HttpResponseRedirect(reverse("flight", args=(flight.id,))) #reverse takes name of view