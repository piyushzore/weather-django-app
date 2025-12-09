from django.contrib import admin
from .models import City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'created_at')
    search_fields = ('name', 'country')
    list_per_page = 20
