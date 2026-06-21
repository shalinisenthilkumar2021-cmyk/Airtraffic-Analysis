import logging

import pandas as pd
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Airport, Flight, FlightData
from .serializers import AirportSerializer, FlightSerializer, FlightDataSerializer
from airtraffic_analysis.settings import BASE_DIR

logger = logging.getLogger('dashboard')

DATA_PATH = BASE_DIR / "data" / "flights.csv"


class AirportListAPIView(generics.ListCreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FlightListAPIView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FlightUploadAPIView(generics.ListCreateAPIView):
    queryset = FlightData.objects.all()
    serializer_class = FlightDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f"Flight data file uploaded via API: {instance.file.name}")


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def flight_summary_api(request):
    """
    Returns aggregate stats computed from the flights CSV dataset —
    a read-only analytics endpoint, useful for external dashboards
    or quick integration testing.
    """
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        logger.error("flights.csv not found for summary API")
        return Response({"error": "Flight dataset not found."}, status=404)

    summary = {
        "total_flights": len(df),
        "total_passengers": int(df["Passengers"].sum()),
        "average_delay_minutes": round(df["Delay_Minutes"].mean(), 2),
        "busiest_destination": df.groupby("Destination")["Passengers"].sum().idxmax(),
    }

    logger.info("Flight summary API called")
    return Response(summary)
