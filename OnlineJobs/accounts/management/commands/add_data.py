from django.core.management.base import BaseCommand
from accounts.models import *
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Add test data to the database'

    def handle(self, *args, **options):
        # Add your test data creation logic here
        user1 = User.objects.create_user(
            username='employer2', password='Employer@123')
        user2 = User.objects.create_user(
            username='employee2', password='Employee@123')
        user1.save()
        user2.save()
        Employee.objects.create(
            user=user2,
            city='EmployeeCity',
            national_id=123456789,
            experience_level='Junior',
            biography='EmployeeBiography'
        )

        Employer.objects.create(
            user=user1,
            job_title="HR MANAGER"

        )
