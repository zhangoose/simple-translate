from django.conf import settings
from rest_framework.permissions import BasePermission
from rest_framework.authentication import get_authorization_header


class ApiTokenPermissions(BasePermission):
    """
    API access is based on whether or not a request contains a valid API token.

    Should be `API_TOKEN` in settings.
    """
    def has_permission(self, request, view):
        key = request.META.get('HTTP_AUTHORIZATION', '')
        if key == settings.API_TOKEN:
            return True
        return False
