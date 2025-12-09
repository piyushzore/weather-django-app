from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, WeatherView, dashboard

router = DefaultRouter()
router.register(r'cities', CityViewSet, basename='city')

urlpatterns = [
    path('', include(router.urls)),
    path('weather/<str:city>/', WeatherView.as_view(), name='weather-by-city'),
    path('dashboard/', dashboard, name='dashboard'),
]
