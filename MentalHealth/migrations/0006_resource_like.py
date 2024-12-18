# Generated by Django 4.1 on 2024-03-10 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("MentalHealth", "0005_remove_event_available_seats_remove_event_booked_by"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resource",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Mental Health", "Mental Health"),
                            ("Stress Management", "Stress Management"),
                            ("Self Care", "Self Care"),
                            ("Motivation", "Motivation"),
                            ("Eating Disorders", "Eating disorders"),
                            ("Anxiety", "Anxiety disorders"),
                            ("Dipression", "Depression"),
                        ],
                        max_length=100,
                    ),
                ),
                ("upload_date", models.DateTimeField(auto_now_add=True)),
                (
                    "uploader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="MentalHealth.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Like",
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
                (
                    "resource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="MentalHealth.resource",
                    ),
                ),
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
