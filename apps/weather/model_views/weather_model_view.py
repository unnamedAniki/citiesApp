from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from apps.weather.models import WeatherValue
from apps.weather.utils.mixins import WeatherMixin, GetWeatherMixin


class WeatherCreateView(LoginRequiredMixin, WeatherMixin, CreateView):

    def get_login_url(self):
        return reverse("user-login")


class WeatherEditView(LoginRequiredMixin, WeatherMixin, UpdateView):

    def get_login_url(self):
        return reverse("user-login")


class WeatherDeleteView(LoginRequiredMixin, DeleteView):
    model = WeatherValue
    success_url = reverse_lazy("weather")

    def get_login_url(self):
        return reverse("user-login")


class WeatherGetView(LoginRequiredMixin, GetWeatherMixin, CreateView):

    def get_login_url(self):
        return reverse("user-login")