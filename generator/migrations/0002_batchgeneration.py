# Generated by Django 5.2 on 2025-05-08 10:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("generator", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BatchGeneration",
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
                ("prompt", models.TextField()),
                ("count", models.PositiveIntegerField()),
                (
                    "language",
                    models.CharField(
                        choices=[("en", "English"), ("ru", "Русский")], max_length=2
                    ),
                ),
                (
                    "file_format",
                    models.CharField(
                        choices=[("zip", "ZIP"), ("csv", "CSV"), ("txt", "TXT")],
                        max_length=3,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
