# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FootballFieldViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'football-fields', FootballFieldViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
