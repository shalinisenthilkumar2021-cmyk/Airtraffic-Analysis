from django.urls import path
from . import api_views

urlpatterns = [
    path('airports/', api_views.AirportListAPIView.as_view(), name='api_airports'),
    path('flights/', api_views.FlightListAPIView.as_view(), name='api_flights'),
    path('upload/', api_views.FlightUploadAPIView.as_view(), name='api_upload'),
    path('summary/', api_views.flight_summary_api, name='api_summary'),
]
