from django.urls import path
from .views import *

urlpatterns = [
    path("", JobListCreateView.as_view())

]
