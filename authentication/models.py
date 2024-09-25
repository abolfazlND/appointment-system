from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    AbstractUser,
)
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(
        self, phone_number, first_name, last_name, role, password=None, **extra_fields
    ):
        if not phone_number:
            raise ValueError(_("The Phone number field must be set"))
        # email = self.normalize_email(email)
        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            role=role,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")
        extra_fields.setdefault("first_name", "Admin")
        extra_fields.setdefault("last_name", "Super")
        return self.create_user(phone_number, password=password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    USER_ROLES = (
        ("admin", "Admin"),
        ("doctor", "Doctor"),
        ("patient", "Patient"),
    )

    phone_number = PhoneNumberField(unique=True, region="IR")
    role = models.CharField(max_length=10, choices=USER_ROLES)  # @TODO set default
    # @TODO use method for save username in filename
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"

    # @TODO install black
    # flake8
    # install https://github.com/astral-sh/ruff
    REQUIRED_FIELDS = ["first_name", "last_name", "role"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
