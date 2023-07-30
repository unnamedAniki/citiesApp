from django import forms
from apps.cities.models import City
from apps.cities.queries import city_queries

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']

    name = forms.CharField(max_length=255)

    def clean_name(self):
        name = self.cleaned_data['name']
        exists_city = city_queries.get_city_by_name(name)
        if exists_city.count() != 0:
            raise forms.ValidationError("This city already exists")
        return name