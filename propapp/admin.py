from django.contrib import admin
from .models import Property,City,State,Prop_Images,News,General_Options 

class CityAdmin(admin.ModelAdmin):
	fieldset = [('City',{'field':['name']}),('Zipcode',{'field':['zipcode']}),('State',{'field':['state.name']})]


class PropertyAdmin(admin.ModelAdmin):
	list_display = ('property_id', 'name', 'city', 'state', 'price', 'date', 'is_available')


class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'state')

class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'referer_link', 'date')

admin.site.register(Property,PropertyAdmin)
admin.site.register(Prop_Images)
admin.site.register(City, CityAdmin)
admin.site.register(State)
admin.site.register(News, NewsAdmin)
admin.site.register(General_Options)


