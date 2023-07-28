from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from .queries import city_queries
from .models import WeatherValue, City


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


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']

    name = forms.CharField(max_length=255)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    @staticmethod
    def user_login(request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        from django.contrib.auth import authenticate
        from django.contrib.auth import login
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        return redirect("/login")

    @staticmethod
    def user_logout(request):
        from django.contrib.auth import logout
        logout(request)
        return redirect("/")


class GraphForm(forms.Form):
    date = forms.DateTimeField()
    city = forms.ModelChoiceField(help_text="Choice city",
                                  empty_label="(Nothing)",
                                  queryset=city_queries.get_all_cities())
