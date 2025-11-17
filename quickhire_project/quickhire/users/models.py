from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        EMPLOYER = "employer", "Employer"
        APPLICANT = "applicant", "Applicant"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Roles.choices)

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"


