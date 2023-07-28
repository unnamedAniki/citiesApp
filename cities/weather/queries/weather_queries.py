import datetime

import pytz as pytz
from django.core.exceptions import ObjectDoesNotExist
from .. import models


def get_weather_by_city_and_date(city_id: int, date: datetime):
    return models.WeatherValue.objects.\
        filter(cities_id=city_id, date__range=(date, date + datetime.timedelta(days=1)))


def get_weather_by_city(city_id: int):
    return models.WeatherValue.objects.\
        filter(cities_id=city_id)


def get_single_weather_by_city_and_date(city_id: int, date: datetime, weather_id: int = 0):
    return models.WeatherValue.objects.\
        filter(cities_id=city_id, date=date).exclude(id=weather_id)
