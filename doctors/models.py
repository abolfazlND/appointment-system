from django.db import models
from authentication.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100, unique=True, default='NotSet')
    bio = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"

class DoctorAvailability(models.Model):
    SLOT_TYPE_CHOICES = [
        ('appointment', 'Appointment'),  # رزرو نوبت برای بیمار
        ('break', 'Break')               # زمان استراحت
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=9)  # Monday, Tuesday, etc.
    start_time = models.TimeField()
    end_time = models.TimeField()

    slot_type = models.CharField(max_length=20, choices=SLOT_TYPE_CHOICES, default='appointment')

    class Meta:
        unique_together = ('doctor', 'day_of_week', 'start_time', 'slot_type')