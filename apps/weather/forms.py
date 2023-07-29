from django import forms
from apps.cities.queries import city_queries


class GraphForm(forms.Form):
    date = forms.DateTimeField()
    city = forms.ModelChoiceField(help_text="Choice city",
                                  empty_label="(Nothing)",
                                  queryset=city_queries.get_all_cities())
