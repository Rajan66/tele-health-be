from django.db import models
from gatekeeper.models import User
from base.models import BaseModel
from worker.models import HealthWorker


class Patient(BaseModel):
    first_name = models.CharField(max_length=20)

    last_name = models.CharField(max_length=20)

    phone = models.CharField(max_length=15)

    address = models.TextField(blank=True, null=True)

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=10,
        choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
    )

    blood_group = models.CharField(max_length=5, blank=True, null=True)

    weight = models.FloatField(blank=True, null=True)

    blood_pressure = models.CharField(max_length=15)

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="patients_created",
    )


def __str__(self):
    return f"{self.first_name} ({self.last_name})"
