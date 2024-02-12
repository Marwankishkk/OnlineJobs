from ast import Try
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    city=models.CharField(max_length=100 ,null=True)
    national_id=models.IntegerField(null=True)
    experience_level=models.CharField(null=True,max_length=200,choices= [
        ('Junior', 'Junior'),
        ('Mid', 'Mid'),
        ('Senior', 'Senior'),
    ])
    biography=models.TextField(null=True)

class Employer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    job_title=models.CharField(max_length=150)
