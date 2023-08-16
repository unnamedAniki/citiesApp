from django.urls import path
from apps.weather.list_views import WeatherListView, CityWeatherListView
from apps.weather.model_views import WeatherCreateView, WeatherEditView, WeatherDeleteView, WeatherGetView


urlpatterns = [
    path('', WeatherListView.as_view(), name='weather'),
    path('<int:id>', CityWeatherListView.as_view(), name='city-weather'),
    path('create/', WeatherCreateView.as_view(), name='weather-create'),
    path('edit/<int:pk>', WeatherEditView.as_view(), name='weather-edit'),
    path('delete/<int:pk>', WeatherDeleteView.as_view(), name='weather-delete'),
    path('get/', WeatherGetView.as_view(), name='get-weather')
]