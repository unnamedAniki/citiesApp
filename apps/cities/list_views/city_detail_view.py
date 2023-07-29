from django.views.generic import ListView
from apps.cities.queries import city_queries


class CityListView(ListView):
    paginate_by = 5
    template_name = "weather/city_list.html"
    context_object_name = "cities"
    queryset = city_queries.get_all_cities()
