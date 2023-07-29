from django import forms

from apps.cities.queries import city_queries
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