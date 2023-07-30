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
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(self.request, 'forms/weather_form.html', {"form": form})
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
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(self.request, 'forms/weather_form.html', {"form": form})

        super().post(self, request, *args, **kwargs)
        return redirect("/weather")


class WeatherDeleteView(LoginRequiredMixin, DeleteView):
    model = WeatherValue
    success_url = reverse_lazy("weather")

    def get_login_url(self):
        return reverse("user-login")