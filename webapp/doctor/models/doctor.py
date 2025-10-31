from django.db import models  # noqa

from base.models import BaseModel

from gatekeeper.models import User
from hospital.models import Department


class Doctor(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="doctor_profile"
    )
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )
    contact = models.CharField(max_length=20, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"
