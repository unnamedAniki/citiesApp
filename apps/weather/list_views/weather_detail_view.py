from datetime import datetime

from django.views.generic import ListView
from apps.weather.queries import weather_queries
from apps.cities.queries import city_queries


class WeatherListView(ListView):
    paginate_by = 5
    template_name = "weather/weather_list.html"
    context_object_name = "weathers"

    def get_queryset(self):
        if self.request.GET.get("city") is not None:
            return weather_queries.get_weather_by_city(self.request.GET.get("city"))
        return city_queries.get_all_cities_with_weather()


class CityWeatherListView(ListView):
    paginate_by = 5
    template_name = "weather/weather_list.html"
    context_object_name = "city_weathers"

    def get_queryset(self):
        city_id = self.request.path.split("/")[-1]
        return weather_queries.get_weather_by_city(city_id)


class DateWeatherListView(ListView):
    paginate_by = 10
    template_name = "weather/weather_list.html"
    context_object_name = "date_weathers"

    def get_queryset(self):
        str_date = self.request.path.split("/")[-1]
        date = datetime.strptime(str_date, "%Y-%m-%d")
        return weather_queries.get_weather_by_date(date)

