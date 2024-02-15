from urllib import request
from django.shortcuts import render
from .permission import IsEmployer
from accounts.models import Employer
from .serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


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


class ApplicationsListCreateView(generics.ListCreateAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsListCreateSerializer

    def post(self, request, job_id, *args, **kwargs):
        current_user = self.request.user
        try:
            employee_instance = Employee.objects.get(user=current_user)
            job_instance = get_object_or_404(Jobs, pk=job_id)
            serializer = ApplicationsListCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(employee=employee_instance, jobs=job_instance)
                return Response({"detail": "You have successfully applied"}, status=status.HTTP_201_CREATED)
        except Employee.DoesNotExist:
            return Response({"detail": "Sign in First"}, status=status.HTTP_400_BAD_REQUEST)


class JobsView(generics.ListAPIView):  # Jobs for the logged in employer
    serializer_class = JobsListCreateSerializer

    def get_queryset(self):
        employer_instance = Employer.objects.get(user=self.request.user)
        return Jobs.objects.filter(employer=employer_instance)


class JobApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationsListCreateSerializer
    permisson_classes = [IsEmployer]
    lookup_field = 'jobs_id'

    def get_queryset(self):
        job_id = self.kwargs.get('jobs_id')
        return Applications.objects.filter(jobs__id=job_id)


class ApplicationStatus(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicationsListCreateSerializer
    permission_classes = [IsEmployer]
    # Specify the name of the URL parameter for the application ID
    lookup_url_kwarg = 'id'
    lookup_field = 'id'  # Specify the field to use for the lookup in the model

    def get_queryset(self):
        job_id = self.kwargs.get('jobs_id')
        application_id = self.kwargs.get('id')
        return Applications.objects.filter(jobs__id=job_id, id=application_id)
