from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, FormView

from .forms import WeatherForm, CityForm, LoginForm, GraphForm
from .models import WeatherValue, City
from .queries import city_queries, weather_queries


def index(request):
    return render(request, "index.html", {"request": request})


def choose_date_for_draw(request):
    if request.method == "POST":
        strdate = request.POST.get("date")
        city = request.POST.get("city")
        date = datetime.strptime(strdate, "%Y-%m-%d").date()
        return HttpResponseRedirect(f"/show?date={date}&city={city}")
    return render(request, "forms/graph_form.html", {"form": GraphForm})


def graphs(request):
    strdate = request.GET.get("date")
    city_id = request.GET.get("city")
    date = datetime.strptime(strdate, "%Y-%m-%d")
    data = weather_queries.get_weather_by_city_and_date(city_id, date)

    if data.count() == 0:
        return render(request, "graph.html")

    weather = [e.value for e in data]
    city = [e.cities.name for e in data]
    time = [f'{e.date.time().hour}:{e.date.time().minute}' for e in data]
    content = dict({
        "date": date.date().isoformat(),
        "weather_data": weather,
        "city_name": city[0],
        "time": time
    })

    return render(request, "graph.html", context=content)

