from django.core.exceptions import ObjectDoesNotExist

from apps.weather.models import WeatherValue
from apps.cities.models import City


def get_all_cities_with_weather():
    return WeatherValue.objects.all()


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
