import datetime

from apps.weather.models import WeatherValue


def get_weather_by_city_and_date(city_id: int, date: datetime):
    return WeatherValue.objects.\
        filter(cities_id=city_id, date__range=(date, date + datetime.timedelta(days=1)))


def get_weather_by_city(city_id: int):
    return WeatherValue.objects.\
        filter(cities_id=city_id)


def get_single_weather_by_city_and_date(city_id: int, date: datetime, weather_id: int = 0):
    return WeatherValue.objects.\
        filter(cities_id=city_id, date=date).exclude(id=weather_id)


def add_or_edit_weather(city_id: int, date: datetime, temperature: float):
    try:
        exists_weather = WeatherValue.objects.get(cities_id=city_id, date=date)
        exists_weather.value = temperature
        exists_weather.save()
    except:
        weather = WeatherValue()
        weather.cities_id = city_id
        weather.date = date
        weather.value = temperature
        weather.save()