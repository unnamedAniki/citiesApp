from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import ProcessFormView

from apps.weather.model_forms import WeatherForm
from apps.weather.models import WeatherValue


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
