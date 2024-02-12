from .models import Jobs
from rest_framework import serializers
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status


class JobsListCreateSerializer(serializers.ModelSerializer):
    employer_name = serializers.SerializerMethodField()

    class Meta():
        model = Jobs
        fields = ['location', 'title', 'experience_level', 'employer_name']

    def get_employer_name(self, obj):
        try:
            employer_instance = obj.employer
            user_instance = employer_instance.user
            return user_instance.username
        except Exception as e:
            return None
