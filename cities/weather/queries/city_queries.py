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
        return models.City.objects.filter(name=city_name)
    except ObjectDoesNotExist:
        return None


def edit_city(city_id: int, new_name:str):
    edit_city = models.City.objects.get(id=city_id)
    edit_city.name = new_name
    edit_city.save()
    return edit_city


def delete_city(city_id: int):
    models.City.objects.filter(id=city_id).delete()
    return True


def add_city(name: str):
    if(models.City.objects.filter(name=name).count() == 0):
        models.City.objects.create(name=name)
        return True
    return False
