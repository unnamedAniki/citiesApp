from django.db import models
from django.forms import forms


class City(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        db_table = "cities_city"

    name = models.CharField(max_length=255)

