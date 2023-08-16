import requests
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import ProcessFormView

from apps.cities.queries import city_queries
from apps.weather.model_forms import WeatherForm, GetWeatherForm
from apps.weather.models import WeatherValue
from apps.weather.queries import weather_queries
from main import settings


class WeatherMixin(ProcessFormView):
    model = WeatherValue
    form_class = WeatherForm
    template_name = "forms/weather_form.html"
    success_url = reverse_lazy("weather")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, 'forms/weather_form.html', {"form": form})
        super().post(self, request, *args, **kwargs)
        return redirect("/weather")


class GetWeatherMixin(ProcessFormView):
    model = WeatherValue
    form_class = GetWeatherForm
    success_url = reverse_lazy("weather")
    template_name = "weather/get_weather.html"

    def post(self, request, *args, **kwargs):
        city_name = request.POST['cities']
        city_id = city_queries.get_city_by_name(city_name)[0]
        url = settings.GEO_API_URI + f"q={city_name}&limit={settings.LIMIT_RESPONCE}&appid={settings.API_KEY}"
        response = requests.get(url=url).json()
        form = self.form_class(request.POST)
        if len(response) == 0:
            form.add_error('cities', 'Nothing to found to this city')
            return render(request, 'weather/get_weather.html', {"form": form})
        latitude = response[0]['lat']
        longitude = response[0]['lon']
        url = settings.WEATHER_API_URI + f"lat={latitude}&lon={longitude}&appid={settings.API_KEY}"
        response = requests.get(url=url).json()['list']
        for weather_data in response:
            temperature = float('{:.1f}'.format(weather_data['main']['temp']+settings.KELVIN_DEGREES))
            weather_queries.add_or_edit_weather(city_id=city_id.id,
                                                date=weather_data['dt_txt'],
                                                temperature=temperature)
        return redirect("/weather")