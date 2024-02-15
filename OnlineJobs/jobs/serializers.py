from .models import *
from rest_framework import serializers
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status


class JobsListCreateSerializer(serializers.ModelSerializer):
    employer_name = serializers.SerializerMethodField()

    class Meta():
        model = Jobs
        fields = ['id', 'location', 'title',
                  'experience_level', 'employer_name']

    def get_employer_name(self, obj):
        try:
            employer_instance = obj.employer
            user_instance = employer_instance.user
            return user_instance.username
        except Exception as e:
            return None


class ApplicationsListCreateSerializer(serializers.ModelSerializer):
    employee_name = serializers.SerializerMethodField()
    job_title = serializers.SerializerMethodField()

    class Meta():
        model = Applications
        fields = ['id', 'status', 'employee_name', 'job_title']

    def get_employee_name(self, obj):
        try:
            employee_instance = obj.employee
            user_instance = employee_instance.user
            return user_instance.username
        except Exception as e:
            return None

    def get_job_title(self, obj):
        job_instance = obj.jobs
        return job_instance.title
