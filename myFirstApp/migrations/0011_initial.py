# Generated by Django 4.1.6 on 2024-04-25 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myFirstApp', '0010_delete_doctor_delete_hospital_delete_patient_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deskripsi', models.CharField(max_length=300)),
                ('urlgambar', models.CharField(max_length=300)),
                ('userid', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='myFirstApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.CharField(max_length=300)),
                ('userid', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='myFirstApp.user')),
            ],
        ),
    ]
