from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView

from apps.cities.model_forms import CityForm
from apps.cities.models import City
from apps.cities.queries import city_queries


class CityCreateView(LoginRequiredMixin, CreateView):
    form_class = CityForm
    template_name = "forms/city_form.html"
    success_url = "/cities"

    def get_login_url(self):
        return reverse("user-login")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(self.request, 'forms/city_form.html', {"form": form})
        super().post(self, request, *args, **kwargs)
        return redirect("/cities")


class CityEditView(LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = "forms/city_form.html"
    success_url = "/cities"

    def get_login_url(self):
        return reverse("user-login")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(self.request, 'forms/city_form.html', {"form": form})
        super().post(self, request, *args, **kwargs)
        return redirect("/cities")


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    success_url = "/cities"

    def get_login_url(self):
        return reverse("user-login")