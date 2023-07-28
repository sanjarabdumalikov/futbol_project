# permissions.py
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Implement logic to check if the user is an admin
        # Admins have full access (GET, POST, PUT, DELETE)
        # Other users (Land Owners and Users) have read-only access (GET)
