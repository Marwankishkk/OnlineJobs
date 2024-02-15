from django.db import models

from accounts.models import Employer, Employee
# Create your models here.


class Jobs(models.Model):
    location = models.CharField(max_length=200)
    description = models.TextField()
    experience_level = models.CharField(null=True, max_length=200, choices=[
        ('Junior', 'Junior'),
        ('Mid', 'Mid'),
        ('Senior', 'Senior'),
    ])
    title = models.CharField(max_length=100)
    employer = models.ForeignKey(
        Employer, on_delete=models.CASCADE, null=True, default=None)


class Applications(models.Model):
    jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), (
        'accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
