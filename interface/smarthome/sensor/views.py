from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from monitor.models import LogicLocation, SensorPrologue, SensorThgr122N, SensorKedsum

def sensor(request, sensorid):
  location = LogicLocation.objects.get(id=sensorid)
  result = eval((location.type).title().replace('_','')).objects.filter(channel=location.channel).order_by("-date")

  paginator = Paginator(result, 20)
  
  page = request.GET.get('page')
  try:
     output = paginator.page(page)
  except PageNotAnInteger:
     # If page is not an integer, deliver first page.
     output = paginator.page(1)
  except EmptyPage:
     # If page is out of range (e.g. 9999), deliver last page of results.
     output = paginator.page(paginator.num_pages)
  
  mix = [{"location":location.location},{"type":(location.type).replace('sensor_','').title()},{"channel":location.channel},{"context": output}] 

  #return render(request, 'sensor/sensor.html', {"context": output})  
  return render(request, 'sensor/sensor.html', {"summary": mix})  
