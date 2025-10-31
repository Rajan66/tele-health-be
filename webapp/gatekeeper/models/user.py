from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from gatekeeper.managers import UserManager


class User(AbstractUser):
    ROLE_CHOICES = [
        ("hospital", "Hospital"),
        ("doctor", "Doctor"),
        ("health_worker", "Health Worker"),
    ]

    username = None

    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default="health_worker"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
