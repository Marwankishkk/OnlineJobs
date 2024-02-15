from django.urls import path
from .views import *

urlpatterns = [
    path("", JobListCreateView.as_view()),
    path('<int:job_id>/apply/',
         ApplicationsListCreateView.as_view()),
    path("applicants", JobsView.as_view()),
    # see the jobs you have posted
    path("applicants/<int:jobs_id>", JobApplicationsView.as_view()),
    path("applicants/<int:jobs_id>/<int:id>/",
         ApplicationStatus.as_view()),    # Accept or reject the application



]
