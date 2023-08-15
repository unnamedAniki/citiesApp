from django import forms
from django.core.exceptions import ValidationError

from apps.cities.models import City
from apps.cities.queries import city_queries


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['id', 'name']
    id = forms.IntegerField(required=False)
    name = forms.CharField(max_length=255)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        city_id = 0
        if cleaned_data.get('id'):
            city_id = cleaned_data.get('id')
        exists_city = city_queries.get_city_by_name_and_id(name, city_id)

        if exists_city.count() != 0:
            self.add_error('name', 'This city already exists')