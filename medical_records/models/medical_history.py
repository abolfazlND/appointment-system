from django.db import models
from ..models import MedicalRecord


class MedicalHistory(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='medical_history')
    condition = models.CharField(max_length=255, help_text="Medical condition or disease")
    diagnosed_at = models.DateField(help_text="Date when the condition was diagnosed")
    treatment_details = models.TextField(blank=True, null=True, help_text="Details of the treatment for the condition")
    resolved_at = models.DateField(blank=True, null=True, help_text="Date when the condition was resolved, if applicable")

    def __str__(self):
        return f"{self.condition} (Diagnosed: {self.diagnosed_at})"
