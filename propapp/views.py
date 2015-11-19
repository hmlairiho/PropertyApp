from django.shortcuts import render
from .models import Property

def index(request):
	propertys_list = Property.objects.order_by('-date')[:5]
	context = {'propertys': propertys_list}

	return render(request, 'propapp/index.html', context)


def show_property(request,property_id,name,date,price,city,state,address):
	
	context = {'id': propertys_id, 'name': name, 'address': address, 'city': city, 'state': state, 'price': price}

	return render(request, 'propapp/show.html', context)
