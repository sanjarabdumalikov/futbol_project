# views.py

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class UserRegistrationView(APIView):
    def post(self, request):
        # Handle user registration here and create a User object
        # Return a response with success message and user details

class ObtainAuthToken(APIView):
    def post(self, request):
