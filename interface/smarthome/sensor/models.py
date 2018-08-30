from django.db import migrations, models

#class Location(models.Model):
#    type = models.TextField(max_length=100)
#    channel = models.IntegerField()
#    location = models.TextField(max_length=200)

#    def __str__(self):
#        return self.location

class LogicLocation(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logic_location'

    def __str__(self):
        return str(self.location) + "  - " + self.type



class SensorKedsum(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    channel = models.CharField(max_length=15, blank=True, null=True)
    temperature = models.CharField(max_length=15, blank=True, null=True)
    humidity = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_kedsum'


class SensorPrologue(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    channel = models.CharField(max_length=15, blank=True, null=True)
    temperature = models.CharField(max_length=15, blank=True, null=True)
    humidity = models.CharField(max_length=15, blank=True, null=True)
    battery = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_prologue'


class SensorThgr122N(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    channel = models.CharField(max_length=15, blank=True, null=True)
    temperature = models.CharField(max_length=15, blank=True, null=True)
    humidity = models.CharField(max_length=15, blank=True, null=True)
    battery = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_thgr122n'
