from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView

from ..models import City
from ..queries import city_queries


class CityCreateView(LoginRequiredMixin, CreateView):
    model = City
    fields = ["name"]
    template_name = "forms/city_form.html"
    success_url = "/cities"

    def get_login_url(self):
        return reverse("user-login")

    def post(self, request, *args, **kwargs):
        form_name = self.request.POST.get("name")
        names = city_queries.get_city_by_name(form_name)
        if names.count() != 0:
            return redirect("/cities/create")
        super().post(self, request, *args, **kwargs)
        return redirect("/cities")


class CityEditView(LoginRequiredMixin, UpdateView):
    model = City
    fields = ["name"]
    template_name = "forms/city_form.html"
    success_url = "/cities"

    def get_login_url(self):
        return reverse("user-login")

    def post(self, request, *args, **kwargs):
        form_name = self.request.POST.get("name")
        names = city_queries.get_city_by_name(form_name)
        if names.count() != 0:
            return redirect("/cities/create")
        super().post(self, request, *args, **kwargs)
        return redirect("/cities")


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    success_url = "/cities"

    def get_login_url(self):
        return reverse("user-login")