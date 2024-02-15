
from rest_framework.permissions import BasePermission
from django.core.exceptions import ObjectDoesNotExist
from .models import Employer  # Import your Employer model


class IsEmployer(BasePermission):
    """
    Custom permission to only allow employers to access the view.
    """

    def has_permission(self, request, view):
        try:
            employer_instance = Employer.objects.get(user=request.user)
            return True  # Permission granted if an Employer instance exists
        except ObjectDoesNotExist:
            return False  # Permission denied if no Employer instance exists
