# serializers.py
from rest_framework import serializers
from .models import LandOwner, FootballField, Reservation

class LandOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandOwner
        fields = '__all__'

class FootballFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballField
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
