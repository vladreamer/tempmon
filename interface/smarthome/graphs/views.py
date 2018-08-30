from django.apps import apps
from django.utils import timezone
from chartit import DataPool, Chart
from datetime import datetime, timedelta
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from monitor.models import LogicLocation, SensorPrologue, SensorThgr122N, SensorKedsum

###################################################################################################################################
## List of the Sensors Models (see above "from monitor.models import LogicLocation, SensorPrologue, SensorThgr122N, SensorKedsum")
###################################################################################################################################
sensor_types_list =['SensorPrologue', 'SensorThgr122N', 'SensorKedsum']
#sensor_types_list =['SensorPrologue']

##########################################
## Prepare Time for axle 'X' on the graph
##########################################
def date_x(date):
    time = date.strftime('%a  %H:%M')
    return time

############################################
## Define LOCATION from table LogicLocation
############################################
def location_ch(sensor,channel):
  result = LogicLocation.objects.filter(type=sensor, channel=channel)
  for location in result:
    return location.location

###################################################
## Define DATAPOOL settings (for Step 1: HIGHCHART) 
###################################################
def datapool_set(type, channel, series_set):
   sensor_type  =  type.lower().replace("sensor", "sensor_")
   location = location_ch(sensor_type, channel)
   date_from = timezone.now() - timedelta(hours=30) 
   if location:
      sensor_location = {'options': {
               'source': apps.get_model('monitor', type).objects.filter(channel=channel, date__gte=date_from)},
               'terms': [
               { location+'_date': 'date'},
               { location+'_Temp(\xb0C)': 'temperature'}]}
   else:
      sensor_location = 'None'
   return sensor_location

def datapool_set_h(type, channel, series_set_h):
   sensor_type  =  type.lower().replace("sensor", "sensor_")
   location = location_ch(sensor_type, channel)
   date_from = timezone.now() - timedelta(hours=30) 
   if location:
      sensor_location_h = {'options': {
               'source': apps.get_model('monitor', type).objects.filter(channel=channel, date__gte=date_from)},
               'terms': [
               { location+'_date': 'date'},
               { location+'_Hum(%)': 'humidity'}]}
   else:
      sensor_location_h = 'None'
   return sensor_location_h

########################################################
## Define CHART settings for XY (for Step 2: HIGHCHART)
########################################################
def chart_set(type, channel, xy_set):
   sensor_type  =  type.lower().replace("sensor", "sensor_")
   location = location_ch(sensor_type, channel)
   if location:
      xy_location = {location+'_date' : [ location+'_Temp(\xb0C)']}
   else:
      xy_location = {}
   return  xy_location
 
def chart_set_h(type, channel, xy_set_h):
   sensor_type  =  type.lower().replace("sensor", "sensor_")
   location = location_ch(sensor_type, channel)
   if location:
      xy_location_h = {location+'_date' : [ location+'_Hum(%)']}
   else:
      xy_location_h = {}
   return  xy_location_h
 
########################################################
## HIGHCHART settings combined from above functions
########################################################
xy = {}
xy_set = xy.copy()
series_set = []
## for each SensorType from sensor_types_list
for type in sensor_types_list:
    ## for each channel 
   for channel in [ 1, 2, 3 ]:
      xy_set.update(chart_set(type, channel, xy_set))       
      if datapool_set(type, channel, series_set) != 'None':  
        series_set += [datapool_set(type, channel, series_set)]
        
xy_h = {}
xy_set_h = xy_h.copy()
series_set_h = []
## for each SensorType from sensor_types_list
for type in sensor_types_list:
    ## for each channel 
   for channel in [ 1, 2, 3 ]:
      xy_set_h.update(chart_set_h(type, channel, xy_set_h))       
      if datapool_set_h(type, channel, series_set_h) != 'None':  
        series_set_h += [datapool_set_h(type, channel, series_set_h)]        

########################################################
##  HIGHCHART from above settings
########################################################
def graphs(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    sensordata = DataPool(
           series=
               series_set
               )

    sensordata_h = DataPool(
           series=
               series_set_h
               )
 

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = sensordata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':
                  xy_set
               }],
            chart_options =
              {'title': {
                   'text': '24H Temperature, \xb0C'},
               'xAxis': {
                     'title': {
                         'text': 'Probes'},
                     'labels': {
                         'rotation': -45, 'align': 'right'}},
               'yAxis': {
                 'title': {
                   'text': 'Temperature in \xb0C'},

                }},
                x_sortf_mapf_mts = (None, date_x, False))

    chh = Chart(
            datasource = sensordata_h,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':
                  xy_set_h
               }],
            chart_options =
              {'title': {
                   'text': '24H Humidity, %'},
               'xAxis': {
                     'title': {
                         'text': 'Probes'},
                     'labels': {
                         'rotation': -45, 'align': 'right'}},
               'yAxis': {
                 'title': {
                   'text': 'Humidity in %'},

                }},
                x_sortf_mapf_mts = (None, date_x, False))
    
    #Step 3: Send the chart object to the template.
    return render(request, 'graphs/graphs.html', {'charts': [cht, chh]})
