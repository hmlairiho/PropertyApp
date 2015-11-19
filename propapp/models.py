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
	property_id = models.AutoField(primary_key=True, default=1)
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=15)
	city = models.ForeignKey(City)
	state = models.ForeignKey(State)
	price = models.IntegerField(default=0)
	date = models.DateTimeField('date published')
	available = models.IntegerField(default=1)
	#images = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	def is_available (self):
		if self.available == 1 :
			return True
		else:
			return False

class general_options(models.Model):
	front_title = models.CharField(max_length=15)

