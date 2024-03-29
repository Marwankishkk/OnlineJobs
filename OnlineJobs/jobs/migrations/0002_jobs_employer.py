# Generated by Django 4.2.10 on 2024-02-09 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_employer"),
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobs",
            name="employer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.employer",
            ),
            preserve_default=False,
        ),
    ]
