from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from monitor.models import LogicLocation, SensorPrologue, SensorThgr122N, SensorKedsum

def sqlrequest(sensor,location):

  request =  """SELECT * FROM  logic_location
             INNER JOIN """+sensor+""" ON
             logic_location.type = """+sensor+""".type
             AND logic_location.channel = """+sensor+""".channel
             AND logic_location.location = '%s'
             ORDER BY date DESC LIMIT 1""" % location

   # converting characters in "sensor" variable to much model name
   # for example sensor_prolongue to SensorProlongue with title().replace('_','')
   # eval() evaluates a string and returns an object for RawQuerySet

  sqlresult = eval(sensor.title().replace('_','')).objects.raw(request)

  for sqlout in sqlresult:
    sensor_type = (sqlout.type).title().replace('Sensor_','')
    outdata = {'id': sqlout.id, 'channel': sqlout.channel, 'type': sensor_type, 'date': sqlout.date, 'location': sqlout.location, 'temp': sqlout.temperature,'humid': sqlout.humidity, 'battery': sqlout.battery}
    return outdata

   # providing information from each sensorl location for the defined sensors as cur.type in LogicLocation

def output():
  infolist = []
  for cur in LogicLocation.objects.order_by('location'):
   if cur.type == 'sensor_thgr122n':
     info  = sqlrequest(cur.type, cur.location)
     infolist.append(info)
   elif cur.type == 'sensor_prologue':
     info = sqlrequest(cur.type, cur.location)
     infolist.append(info)
   elif cur.type == 'sensor_kedsum':
     info = sqlrequest(cur.type, cur.location)
     infolist.append(info)
  return infolist 
 
@login_required 
def index(request):
  return render(request, 'monitor/home.html', {"context": output()})

@login_required 
def video(request):
  #return render(request, 'monitor/basic.html', {'content':['Live Video from Camera1 and Camera2']})
  return render(request, 'monitor/video.html')
