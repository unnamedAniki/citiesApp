from django.views.generic import ListView
from ..queries import city_queries


class CityDetailView(ListView):
    paginate_by = 5
    template_name = "weather/city_list.html"
    context_object_name = "cities"
    queryset = city_queries.get_all_cities()
