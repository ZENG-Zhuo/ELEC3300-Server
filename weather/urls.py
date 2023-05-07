from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.get_weather, name='weather'),
    path('forecast/', views.get_forecast, name='forecast'),
]