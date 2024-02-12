from django.shortcuts import render

from accounts.models import Employer
from .serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Jobs
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsListCreateSerializer

    def post(self, request, *args, **kwargs):
        current_user = self.request.user
        try:
            employer_instance = Employer.objects.get(user=current_user)
            print("employer found")
            serializer = JobsListCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(employer=employer_instance)
                return Response({"detail": "Job created successfully by employer."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"detail": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
        except Employer.DoesNotExist:
            return Response({"detail": "You don't have permission to create a job."}, status=status.HTTP_400_BAD_REQUEST)
