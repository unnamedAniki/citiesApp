from django.views.generic import ListView
from ..queries import city_queries, weather_queries


class WeatherDetailView(ListView):
    paginate_by = 5
    template_name = "weather/weather_list.html"
    context_object_name = "weathers"

    def get_queryset(self):
        if self.request.GET.get("city") is not None:
            print(self.request.GET.get("city"))
            return weather_queries.get_weather_by_city(self.request.GET.get("city"))
        return city_queries.get_all_cities_with_weather()
