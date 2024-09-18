from django.db import models
from authentication.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Patient(models.Model): 
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=gender_choices)
    emergency_contact = PhoneNumberField(blank=True, null=True) # Emergency call
    medical_info = models.JSONField(
        blank=True,
        null=True,
        help_text="Store medical data such as allergies, medications, etc."
        )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name()
