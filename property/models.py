from django.db import models

class State(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=30)
	zipcode = models.CharField(max_length=5)
	state = models.ForeignKey(State)

	def __str__(self):
		return self.name

class Property(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=15)
	city = models.ForeignKey(City)
	state = models.ForeignKey(State)
	code = models.CharField(max_length=50)
	date = models.DateTimeField('date published')
	available = models.IntegerField(default=1)

	def __str__(self):
		return self.name