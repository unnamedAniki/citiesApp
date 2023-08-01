from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from apps.cities.models import City
from apps.cities.utils.mixins import CityMixin


class CityCreateView(LoginRequiredMixin, CityMixin, CreateView):
    def get_login_url(self):
        return reverse("user-login")


class CityEditView(LoginRequiredMixin, CityMixin, UpdateView):
    def get_login_url(self):
        return reverse("user-login")


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    success_url = reverse_lazy("cities")

    def get_login_url(self):
        return reverse("user-login")
