from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name ='index') ,
    url(r'^registration$', views.create_user, name='registration'),
    url(r'^success$', views.success, name='success'),
    url(r'^login$', views.login, name='login'),
]
