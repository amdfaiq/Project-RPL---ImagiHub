# Generated by Django 4.1.6 on 2024-04-25 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0009_rename_massage_doctor_reservation_message_doctor_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Session',
        ),
    ]
