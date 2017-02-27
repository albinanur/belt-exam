from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name ='index') ,
	url(r'^wish_items/create$', views.create ,name ='create'),
	url(r'^wish_items/add$', views.add_new_wish ,name ='add_new_wish'),
	url(r'^wish_items/(?P<id>\d+)$', views.wish ,name ='wish'),
	url(r'^(?P<id>\d+)/delete$', views.delete, name ='delete'),
	url(r'^wish_items/(?P<id>\d+)/add_to_my$', views.add_to_my, name ='add_to_my'),
	url(r'^(?P<id>\d+)/remove$', views.remove, name ='remove'),



]
