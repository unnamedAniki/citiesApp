from django.core.exceptions import ObjectDoesNotExist

from .. import models


def get_all_cities_with_weather():
    return models.WeatherValue.objects.all()


def get_all_cities():
    return models.City.objects.all()


def get_city_by_id(city_id: int):
    try:
        return models.City.objects.get(id=city_id)
    except ObjectDoesNotExist:
        return None


def get_city_by_name(city_name: str):
    try:
        return models.City.objects.get(name=city_name)
    except ObjectDoesNotExist:
        return None