from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from ..models import WeatherValue
from ..queries import weather_queries


class WeatherCreateView(LoginRequiredMixin, CreateView):
    model = WeatherValue
    fields = ['date', 'value', 'cities']
    template_name = "forms/weather_form.html"
    success_url = "/weather"

    def get_login_url(self):
        return reverse("user-login")

    def post(self, request, *args, **kwargs):
        form_city = self.request.POST.get("city")
        strdate = self.request.POST.get("date")
        time = datetime.strptime(strdate, "%Y-%m-%d %H:%M").date()
        print(strdate)
        weathers = weather_queries.get_weather_by_city_and_date(form_city, time)
        if weathers.count() != 0:
            return redirect("/weather/create")
        super().post(self, request, *args, **kwargs)
        return redirect("/weather")


class WeatherEditView(LoginRequiredMixin, UpdateView):
    model = WeatherValue
    fields = ['date', 'value', 'cities']
    template_name = "forms/weather_form.html"
    success_url = "/weather"

    def get_login_url(self):
        return reverse("user-login")

    def post(self, request, *args, **kwargs):
        form_city = self.request.POST.get("city")
        strdate = self.request.POST.get("date")
        time = datetime.strptime(strdate, "%Y-%m-%d %H:%M").date()
        weathers = weather_queries.get_weather_by_city_and_date(form_city, time)
        if weathers.count() != 0:
            return redirect(f"/weather/edit/{self.model.pk}")
        super().post(self, request, *args, **kwargs)
        return redirect("/weather")


class WeatherDeleteView(LoginRequiredMixin, DeleteView):
    model = WeatherValue
    success_url = "/weather"

    def get_login_url(self):
        return reverse("user-login")