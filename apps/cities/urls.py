from django.urls import path
from apps.cities.list_views import CityListView
from apps.cities.model_views import CityCreateView, CityEditView, CityDeleteView

urlpatterns = [
    path('', CityListView.as_view(), name='cities'),
    path('create/', CityCreateView.as_view(), name='cities-create'),
    path('edit/<int:pk>', CityEditView.as_view(), name='cities-edit'),
    path('delete/<int:pk>', CityDeleteView.as_view(), name='cities-delete'),
]
