from datetime import datetime

from django import forms

from apps.cities.queries import city_queries
from apps.weather.queries import weather_queries
from apps.weather.models import WeatherValue


class WeatherForm(forms.ModelForm):
    class Meta:
        model = WeatherValue
        fields = ['date', 'value', 'cities']

    date = forms.DateTimeField(label="Date",
                               required=True,
                               help_text="Choose date and time")
    value = forms.FloatField(label="Value",
                             help_text="Input temperature value")
    cities = forms.ModelChoiceField(help_text="Choice city",
                                    empty_label="(Nothing)",
                                    queryset=city_queries.get_all_cities())

    def clean_value(self):
        data = self.cleaned_data['value']
        if data < -50 or data > 50:
            raise forms.ValidationError('Temperature must be between -50 and +50 degrees')
        return data

    def clean_cities(self):
        current_keys_value = list(self.cleaned_data.keys())

        if not ['date', 'value', 'cities'] == current_keys_value:
            raise forms.ValidationError('You must fill all fields')
        cities = self.cleaned_data['cities']
        date = self.cleaned_data['date']
        exist_weather = weather_queries.get_single_weather_by_city_and_date(cities.id, date)
        if exist_weather.count() != 0:
            raise forms.ValidationError('Temperature for this city and time already exists')
        return cities
