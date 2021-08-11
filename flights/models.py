from django.db import models

# Create your models here.Models is python class
#2nd added
class Airport(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.city} ({self.code})"




#1st added
class Flight(models.Model):
	#origin = models.CharField(max_length=64) #after adding Airport class we modify it
	origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
	#destination = models.CharField(max_length=64)#after adding Airport class we modify it
	destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
	duration = models.IntegerField()

	def __str__(self):
		return f"{self.id} : {self.origin} to {self.destination}"
	#added at testing part of tutorial	
	def is_valid_flight(self):
		return self.origin != self.destination and self.duration >0

#3rd added
class Passenger(models.Model):
	first = models.CharField(max_length=64)
	last = models.CharField(max_length=64)
	flights = models.ManyToManyField(Flight, blank=True,related_name="passengers") #  models.ManyToManyField it means this class has
																				   # many to many relationship to other sql table.
																				   #blank =True means can be empty. Related_name helps
																				   #to find all passenges related to that fligt.
	def __str__(self):
		return f"{self.first} {self.last}"