from django.conf.urls import url
from . import views

urlpatterns = [ 
	url(r'^$', views.index, name='index'), 
	url(r'^(?P<property_id>[0-9]+)/$', views.show_property, name='show_property'),
]