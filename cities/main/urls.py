"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from weather import views

from weather.form_views.login_view import LoginFormView, LogoutFormView
from weather.model_views.city_model_view import CityCreateView, CityEditView, CityDeleteView
from weather.model_views.weather_model_view import WeatherCreateView, WeatherEditView, WeatherDeleteView
from weather.list_views.city_detail_view import CityDetailView
from weather.list_views.weather_detail_view import WeatherDetailView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-login'),
    path('', views.index, name='index'),
    path('login/', LoginFormView.as_view(), name='user-login'),
    path('logout/', LogoutFormView.as_view(), name='user-logout'),
    path('weather/', WeatherDetailView.as_view()),
    path('weather/create/', WeatherCreateView.as_view(), name='weather-create'),
    path('weather/edit/<int:pk>', WeatherEditView.as_view(), name='weather-edit'),
    path('weather/delete/<int:pk>', WeatherDeleteView.as_view(), name='weather-delete'),
    path('cities/', CityDetailView.as_view()),
    path('cities/create/', CityCreateView.as_view(), name='cities-create'),
    path('cities/edit/<int:pk>', CityEditView.as_view(), name='cities-edit'),
    path('cities/delete/<int:pk>', CityDeleteView.as_view(), name='cities-delete'),
    path('graphs/', views.choose_date_for_draw, name='date-for-draw-graph'),
    path('show/', views.graphs, name='graphs')
]
