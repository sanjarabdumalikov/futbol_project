from django.urls import path
from .views import (AllCreatePlaceView,DetailUpdateDeleteApiView,RUDView,AllCreatePlaceView)
urlpatterns = [
    path('',AllCreatePlaceView.as_view()),
    path('<pk>/',DetailUpdateDeleteApiView.as_view()),
    path('booking/',AllCreatePlaceView.as_view()),
    path('booking/<pk>/',RUDView.as_view())
]