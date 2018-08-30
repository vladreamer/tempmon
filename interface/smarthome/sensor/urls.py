from django.conf.urls import url, include
from . import views

urlpatterns = [ url(r'^(\d+)/$', views.sensor, name="sensor") ]
