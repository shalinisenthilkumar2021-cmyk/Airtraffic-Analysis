from django.contrib import admin
from .models import Airport, Flight, FlightData


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'country']


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = [
        'flight_no',
        'airport',
        'passengers',
        'delay',
        'status'
    ]


@admin.register(FlightData)
class FlightDataAdmin(admin.ModelAdmin):
    list_display = [
        'file',
        'uploaded_at'
    ]