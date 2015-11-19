from django.shortcuts import render
from .models import Property

def index(request):
	propertys_list = Property.objects.order_by('-date')[:5]
	context = {'propertys': propertys_list}

	return render(request, 'propapp/index.html', context)


def show_property(request,property_id):
	propertys_list = Property.objects.get(property_id = property_id)
	context = {"propertys_list": propertys_list}

	return render(request, 'propapp/show_property.html', context)
