from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, first_name, last_name, role, password=None, **extra_fields):
        if not phone_number:
            raise ValueError(_('The Phone number field must be set'))
        #email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, first_name=first_name, last_name=last_name, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db) 
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('first_name', 'Admin')
        extra_fields.setdefault('last_name', 'Super')
        return self.create_user(phone_number, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    first_name = models.CharField(max_length=30, blank=False, default="unknown")
    last_name = models.CharField(max_length=30, blank=False, default="unknown")
    phone_number = PhoneNumberField(unique=True, region='IR')
    role = models.CharField(max_length=10, choices=USER_ROLES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='doctor_profiles/', blank=True, null=True)
    

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name','last_name', 'role']

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")