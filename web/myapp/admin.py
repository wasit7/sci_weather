from django.contrib import admin

from .models import Weather

# Register your models here
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('time', 'nodeid', 'temp', 'humi', 'israin')

# Register your models here.
admin.site.register(Weather, WeatherAdmin)
