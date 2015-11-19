from django.contrib import admin
from .models import Property
from .models import City
from .models import State

class CityAdmin(admin.ModelAdmin):
	fieldset = [('City',{'field':['name']}),('Zipcode',{'field':['zipcode']}),('State',{'field':['state.name']})]


class PropertyAdmin(admin.ModelAdmin):
	list_display = ('property_id', 'name', 'city', 'state', 'price', 'date', 'is_available')


class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'state')

admin.site.register(Property)
admin.site.register(City, CityAdmin)
admin.site.register(State)

