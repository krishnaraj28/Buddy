# Generated by Django 4.1 on 2024-03-17 04:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("MentalHealth", "0007_slot_booking"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Booking",
        ),
        migrations.DeleteModel(
            name="Slot",
        ),
    ]
