from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Employee, Employer
from .serializers import EmployeeCreateListSerializer, EmployerCreateListSeriallizer, UserSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class UserCreateListView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
class EmployeeCreateView(generics.CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeCreateListSerializer
    permission_classes=[IsAuthenticated]
    
    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(user=current_user)
class EmployeeListUpdateView(generics.RetrieveUpdateAPIView):
    #queryset=Employee.objects.all()
    serializer_class=EmployeeCreateListSerializer
    lookup_field='pk'
    def get_object(self):
        # Retrieve the Employee instance based on the currently logged-in user
        return Employee.objects.get(user=self.request.user)

class EmployerCreateView(generics.CreateAPIView):
    queryset=Employer.objects.all()
    serializer_class=EmployerCreateListSeriallizer
    permission_classes=[IsAuthenticated]
    def perform_create(self,serializer):
        current_user=self.request.user
        serializer.save(user=current_user)

class EmployerListUpdateView(generics.RetrieveUpdateAPIView):
    #queryset=Employee.objects.all()
    serializer_class=EmployerCreateListSeriallizer
    lookup_field='pk'
    def get_object(self):
        # Retrieve the Employee instance based on the currently logged-in user
        return Employer.objects.get(user=self.request.user)

