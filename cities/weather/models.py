import datetime

from django.db import models


class City(models.Model):
    def __str__(self):
        return self.name

    def __int__(self):
        return self.id

    name = models.CharField(max_length=255)


class WeatherValue(models.Model):
    def __str__(self):
        return f"city: {self.cities.name}, temp: {self.value}C"
    date = models.DateTimeField(default=datetime.datetime.now())
    value = models.FloatField(default=0)
    cities = models.ForeignKey(City, on_delete=models.CASCADE)
