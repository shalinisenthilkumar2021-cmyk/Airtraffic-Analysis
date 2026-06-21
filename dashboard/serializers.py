from rest_framework import serializers
from .models import Airport, Flight, FlightData


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['id', 'name', 'city', 'country']


class FlightSerializer(serializers.ModelSerializer):
    airport_name = serializers.CharField(source='airport.name', read_only=True)

    class Meta:
        model = Flight
        fields = ['id', 'flight_no', 'airport', 'airport_name', 'passengers', 'delay', 'status']


class FlightDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightData
        fields = ['id', 'file', 'uploaded_at']
        read_only_fields = ['uploaded_at']
