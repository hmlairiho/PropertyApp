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
	property_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=15)
	city = models.ForeignKey(City)
	state = models.ForeignKey(State)
	price = models.IntegerField(default=0)
	date = models.DateTimeField('date published')
	available = models.IntegerField(default=1)

	def __str__(self):
		return self.name

	def is_available (self):
		if self.available == 1 :
			return True
		else:
			return False

class General_Options(models.Model):
	front_title = models.CharField(max_length=30)

	def __str__(self):
		return self.front_title

class News(models.Model):
	title = models.CharField(max_length=25)
	referer_link = models.CharField(max_length=150)
	date = models.DateTimeField('date published')
	image_link = models.CharField(max_length=150,default=None)

	def __str__(self):
		return self.title

class Prop_Images(models.Model):
	property_id = models.ForeignKey(Property)
	name = models.CharField(max_length=10)
	image_id = models.AutoField(primary_key=True, default=1)
	image_path = models.CharField(max_length=20)
	image_thumb = models.CharField(max_length=20)





