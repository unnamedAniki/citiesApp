from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from apps.weather.model_forms import WeatherForm
from apps.weather.models import WeatherValue
from apps.weather.queries import weather_queries


class WeatherCreateView(LoginRequiredMixin, CreateView):
    model = WeatherValue
    form_class = WeatherForm
    template_name = "forms/weather_form.html"
    success_url = "/weather"

    def get_login_url(self):
        return reverse("user-login")

    def post(self, request, *args, **kwargs):
        form_city = self.request.POST.get("cities")
        strdate = self.request.POST.get("date")
        time = datetime.strptime(strdate, "%Y-%m-%d %H:%M")
        weathers = weather_queries.get_single_weather_by_city_and_date(form_city, time)

        if weathers.count() != 0:
            return redirect("/weather/create")
        super().post(self, request, *args, **kwargs)
        return redirect("/weather")


class WeatherEditView(LoginRequiredMixin, UpdateView):
    model = WeatherValue
    form_class = WeatherForm
    template_name = "forms/weather_form.html"
    success_url = "/weather"

    def get_login_url(self):
        return reverse("user-login")

    def post(self, request, *args, **kwargs):
        data = self.request.POST
        form_city = data.get("cities")
        strdate = data.get("date")
        time = datetime.strptime(strdate, "%Y-%m-%d %H:%M")
        weathers = weather_queries.get_single_weather_by_city_and_date(form_city, time, self.get_object().id)

        if weathers.count() != 0:
            return redirect(f"/weather/edit/{self.get_object().id}")
        super().post(self, request, *args, **kwargs)
        return redirect("/weather")


class WeatherDeleteView(LoginRequiredMixin, DeleteView):
    model = WeatherValue
    success_url = reverse_lazy("weather")

    def get_login_url(self):
        return reverse("user-login")