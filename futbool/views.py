from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import Place , Booking
from rest_framework.response import Response
from .serializers import PlaceSerializer ,BookingSerializer
# Create your views here.
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class AllCreatePlaceView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class DetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class AllCreateBookingView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = BookingSerializer


class DetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = BookingSerializer