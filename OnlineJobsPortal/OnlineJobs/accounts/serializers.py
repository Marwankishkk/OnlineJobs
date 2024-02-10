from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee, Employer


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['id', 'username', 'email', 'password']


class EmployeeCreateListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta():
        model = Employee
        fields = ["name", 'biography', "city",
                  "national_id", "experience_level"]

    def get_name(self, obj):
        user = obj.user
        return user.username


class EmployerCreateListSeriallizer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta():
        model = Employer
        fields = ["name", "job_title"]

    def get_name(self, obj):
        user = obj.user
        return user.username
