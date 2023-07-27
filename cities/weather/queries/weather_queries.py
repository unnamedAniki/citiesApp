import datetime

import pytz as pytz
from django.core.exceptions import ObjectDoesNotExist
from .. import models


def get_weather_by_city_and_date(city_id: int, date: datetime):
    try:
        return models.WeatherValue.objects.filter(cities_id=city_id,
                                                  date__range=(date, date + datetime.timedelta(days=1)))
    except ObjectDoesNotExist:
        return None


def edit_weather(weather_id: int, date: str, value: float, city_id: int):
    new_record = models.WeatherValue.objects.get(id=weather_id)
    new_record.date = date
    new_record.value = value
    new_record.city_id = city_id
    new_record.save()
    return new_record


def add_weather(date: str, value: float, city_id: int):
    if (models.WeatherValue.objects.filter(date=date, value=value, cities_id=city_id).count() == 0):
        models.WeatherValue.objects.create(date=date, value=value, cities_id=city_id)
        return True
    return False


def delete_weather(weather_id: int):
    models.WeatherValue.objects.filter(id=weather_id).delete()
    return True