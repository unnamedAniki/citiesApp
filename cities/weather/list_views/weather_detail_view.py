from django.views.generic import ListView
from ..queries import city_queries


class WeatherDetailView(ListView):
    paginate_by = 5
    template_name = "weather/weather_list.html"
    context_object_name = "weathers"
    queryset = city_queries.get_all_cities_with_weather()