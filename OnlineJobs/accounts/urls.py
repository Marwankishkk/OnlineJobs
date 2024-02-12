from django.urls import path
from .views import *

urlpatterns = [
    path("users/",UserCreateListView.as_view()),
    path("users/employee/profile",EmployeeListUpdateView.as_view()),
    path("users/employee",EmployeeCreateView.as_view()),
    path("users/employer/",EmployerCreateView.as_view()),
    path("users/employer/profile",EmployerListUpdateView.as_view()),

]
