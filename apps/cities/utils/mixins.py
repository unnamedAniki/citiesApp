from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import ProcessFormView

from apps.cities.model_forms import CityForm
from apps.cities.models import City


class CityMixin(ProcessFormView):
    model = City
    form_class = CityForm
    template_name = "forms/city_form.html"
    success_url = reverse_lazy("cities")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(form.errors)
        if not form.is_valid():
            return render(self.request, 'forms/city_form.html', {"form": form})
        super().post(self, request, *args, **kwargs)
        return redirect("cities")
