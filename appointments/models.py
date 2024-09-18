from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.user.last_name} on {self.date}"
