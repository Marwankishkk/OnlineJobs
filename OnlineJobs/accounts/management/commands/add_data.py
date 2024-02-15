from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Employee, Employer
from jobs.models import Jobs, Applications


class Command(BaseCommand):
    help = 'Custom command to add dummy data to the database'

    def handle(self, *args, **options):
        # Your data creation logic here
        employee30_user = User.objects.create(
            username='marwan30employee', email='marwan30@example.com')
        employee30_user.set_password('password123')
        employee30_user.save()
        employee30 = Employee.objects.create(user=employee30_user)

        employee40_user = User.objects.create(
            username='marwan40employee', email='marwan40@example.com')
        employee40_user.set_password('securepassword')
        employee40_user.save()
        employee40 = Employee.objects.create(user=employee40_user)

        employer_user = User.objects.create(
            username='marwanemployer', email='marwanemployer@example.com')
        employer_user.set_password('strongpassword')
        employer_user.save()
        employer = Employer.objects.create(user=employer_user)

        job1 = Jobs.objects.create(
            title='Software eng',
            description='junior software eng',
            experience_level='Junior',
            location='New capital',
            employer=employer
        )

        job2 = Jobs.objects.create(
            title='UI UX',
            description='MID UI UX',
            experience_level='Mid',
            location='ASWAN',
            employer=employer
        )

        Applications.objects.create(jobs=job1, employee=employee30)
        Applications.objects.create(jobs=job2, employee=employee30)
        Applications.objects.create(jobs=job1, employee=employee40)
        Applications.objects.create(jobs=job2, employee=employee40)
