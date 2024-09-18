from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    diagnosis = models.TextField()  # تشخیص بیماری
    treatment = models.TextField()  # درمان پیشنهادی
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Medical Record for {self.patient.user.get_full_name()} by Dr. {self.doctor.user.last_name}"
