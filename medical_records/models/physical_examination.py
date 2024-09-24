from django.db import models
from ..models import MedicalRecord

class PhysicalExamination(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='physical_examinations')
    
    # Vital signs ??????????????????????????????????????????
    blood_pressure_systolic = models.PositiveIntegerField(help_text="Systolic blood pressure (e.g., 120 mmHg)")
    blood_pressure_diastolic = models.PositiveIntegerField(help_text="Diastolic blood pressure (e.g., 80 mmHg)")
    heart_rate = models.PositiveIntegerField(help_text="Heart rate in beats per minute (e.g., 72 bpm)")
    height = models.DecimalField(max_digits=5, decimal_places=2, help_text="Height in meters (e.g., 1.75)")
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight in kilograms (e.g., 70.5)")
    #not sure
    bmi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Body Mass Index")
    
    # General examination results
    general_exam_results = models.TextField(help_text="General examination results (e.g., ears, nose, throat, heart, lungs)")
    
    # Abnormal findings
    abnormal_findings = models.TextField(blank=True, null=True, help_text="Abnormal findings (e.g., abnormal heart or lung sounds)")
    
    notes = models.TextField(blank=True, null=True, help_text="Additional notes about the physical examination")

    def __str__(self):
        return f"Physical exam on {self.medical_record.patient}"

    def calculate_bmi(self):
        self.bmi = self.weight / (self.height ** 2)
        self.save()
        # TODO update function

