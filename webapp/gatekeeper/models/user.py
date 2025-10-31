from base.models import BaseModel  # noqa

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from gatekeeper.managers import UserManager


class User(AbstractUser, BaseModel):
    ROLE_CHOICES = [
        ("hospital", "Hospital"),
        ("doctor", "Doctor"),
        ("health_worker", "Health Worker"),
        ("super_admin", "Super Admin"),
    ]

    username = None

    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default="super_admin"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
