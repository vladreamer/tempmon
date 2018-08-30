from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from monitor.models import LogicLocation, SensorPrologue, SensorThgr122N

urlpatterns = [ url(r'^$', ListView.as_view(queryset=SensorPrologue.objects.all().order_by("-date")[:10], template_name="logic/logic.html")) ]
