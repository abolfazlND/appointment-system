from django.db import models
from ..models import MedicalRecord

ALLERGY_TYPES = [
                ('food', 'Food'),
                ('drug', 'Drug'),
                ('environmental', 'Environmental'),
                ('other', 'Other'),
            ]
SEVERITY_CHOICES = [
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ]

class Allergy(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='allergies')
    allergen = models.CharField(max_length=255, help_text="Name of the allergen")
    allergy_type = models.CharField(max_length=50, choices= ALLERGY_TYPES, default='food', help_text="Type of allergy")
    reaction = models.CharField(max_length=255, blank=True, null=True, help_text="Describe the allergic reaction")
    severity = models.CharField(max_length=50, choices=SEVERITY_CHOICES, help_text="Severity of the allergy")
    notes = models.TextField(blank=True, null=True, help_text="Additional symptoms or notes")

    def __str__(self):
        return f"Allergy: {self.allergen} (Severity: {self.severity})"
