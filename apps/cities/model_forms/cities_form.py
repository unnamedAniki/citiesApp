from django import forms
from apps.cities.models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']

    name = forms.CharField(max_length=255)
