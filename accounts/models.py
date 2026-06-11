from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ADMIN = "ADMIN"
    MEMBER = "MEMBER"

    ROLE_CHOICES = [
        (ADMIN, "Administrateur"),
        (MEMBER, "Membre"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=MEMBER,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username