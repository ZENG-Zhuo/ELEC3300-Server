from django.shortcuts import render
from django.http import HttpResponse
import requests
import sys

def get_weather(request):
    requests_result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')
    django_response = HttpResponse(
        content=requests_result.content,
        status=requests_result.status_code,
        content_type=requests_result.headers['Content-Type']
        )
    return django_response

def get_forecast(request):
    requests_result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en')
    django_response = HttpResponse(
        content=requests_result.content,
        status=requests_result.status_code,
        content_type=requests_result.headers['Content-Type']
        )
    return django_response
