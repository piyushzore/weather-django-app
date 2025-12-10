from rest_framework import viewsets
from .models import City
from .serializers import CitySerializer

import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class WeatherView(APIView):
    """
    GET /api/weather/<city>/
    Returns live weather data for the given city
    """

    def get(self, request, city):
        api_key = getattr(settings, 'OPENWEATHER_API_KEY', None)

        if not api_key:
            return Response(
                {'error': 'OpenWeather API key not configured'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            return Response(
                {'error': 'Failed to fetch weather data', 'details': str(e)},
                status=status.HTTP_502_BAD_GATEWAY
            )

        return Response(data, status=status.HTTP_200_OK)

def dashboard(request):
    """
    Renders the weather dashboard page
    """
    return render(request, 'core/dashboard.html')

from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "success": True,
        "message": "Weather API is live ✅",
        "endpoints": {
            "Cities": "/api/cities/",
            "Weather": "/api/weather/Mumbai/",
            "Dashboard": "/api/dashboard/"
        }
    })

