# Generated by Django 4.2.10 on 2024-02-09 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_employer"),
        ("jobs", "0002_jobs_employer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobs",
            name="employer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.employer",
            ),
        ),
    ]
