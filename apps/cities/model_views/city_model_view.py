from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
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
        form_name = self.request.POST.get("name")
        names = city_queries.get_city_by_name(form_name)
        if names is not None:
            return redirect("/cities/create")
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
        form_name = self.request.POST.get("name")
        names = city_queries.get_city_by_name(form_name)
        if names is not None:
            return redirect(f"/cities/edit/{self.get_object().id}")
        super().post(self, request, *args, **kwargs)
        return redirect("/cities")


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    success_url = "/cities"

    def get_login_url(self):
        return reverse("user-login")