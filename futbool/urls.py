from django.urls import path
from .views import (AllCreatePlaceView,DetailUpdateDeleteApiView)
urlpatterns = [
    path('',AllCreatePlaceView.as_view()),
    path('<pk>/',DetailUpdateDeleteApiView.as_view())
]