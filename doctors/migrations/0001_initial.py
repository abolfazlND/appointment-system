# Generated by Django 5.1.1 on 2024-09-16 23:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=100)),
                ('license_number', models.CharField(default='NotSet', max_length=100, unique=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=9)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('slot_type', models.CharField(choices=[('appointment', 'Appointment'), ('break', 'Break')], default='appointment', max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
            ],
            options={
                'unique_together': {('doctor', 'day_of_week', 'start_time', 'slot_type')},
            },
        ),
    ]
