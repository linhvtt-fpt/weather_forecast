from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=50)
    lon = models.DecimalField(max_digits=7, decimal_places=4)
    lat = models.DecimalField(max_digits=4, decimal_places=2)
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    updated_time = models.DateTimeField(auto_now=True)
    tempC = models.FloatField()
