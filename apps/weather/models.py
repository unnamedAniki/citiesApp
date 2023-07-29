import datetime

from django.db import models
from apps.cities.models import City


class WeatherValue(models.Model):
    def __str__(self):
        return f"city: {self.cities.name}, temp: {self.value}C"

    class Meta:
        db_table = "cities_weathervalue"

    date = models.DateTimeField(default=datetime.datetime.now())
    value = models.FloatField(default=0)
    cities = models.ForeignKey(City, on_delete=models.CASCADE)
