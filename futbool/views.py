# views.py
from rest_framework import viewsets
from .models import LandOwner, FootballField, Reservation
from .serializers import LandOwnerSerializer, FootballFieldSerializer, ReservationSerializer

class LandOwnerViewSet(viewsets.ModelViewSet):
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerSerializer

class FootballFieldViewSet(viewsets.ModelViewSet):
    queryset = FootballField.objects.all()
    serializer_class = FootballFieldSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
