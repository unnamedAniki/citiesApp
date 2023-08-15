from django.core.exceptions import ObjectDoesNotExist

from apps.weather.models import WeatherValue
from apps.cities.models import City


def get_all_cities_with_weather():
    return WeatherValue.objects.all()


def get_all_weathers_by_city(city_id: int):
    return WeatherValue.objects.filter(cities_id=city_id)


def get_all_cities():
    return City.objects.all()


def get_city_by_id(city_id: int):
    try:
        return City.objects.filter(id=city_id)
    except ObjectDoesNotExist:
        return None


def get_city_by_name(city_name: str):
    try:
        return City.objects.filter(name=city_name)
    except ObjectDoesNotExist:
        return None


def get_city_by_name_and_id(city_name: str, city_id: int):
    try:
        return City.objects.filter(name=city_name).exclude(id=city_id)
    except ObjectDoesNotExist:
        return None