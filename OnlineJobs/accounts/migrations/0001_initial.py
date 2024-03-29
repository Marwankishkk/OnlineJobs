# Generated by Django 4.2.10 on 2024-02-06 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(max_length=100)),
                ("national_id", models.IntegerField()),
                (
                    "experience_level",
                    models.CharField(
                        choices=[
                            ("Junior", "Junior"),
                            ("Mid", "Mid"),
                            ("Senior", "Senior"),
                        ],
                        max_length=200,
                    ),
                ),
                ("biography", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
