from django.db import models
from base.models import BaseModel

from patient.models import Patient
from doctor.models.doctor import Doctor
from gatekeeper.models.user import User


class Report(BaseModel):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="reports"
    )
    doctor = patient = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="reports",
        blank=True,
        null=True,
    )

    created_by = (
        models.ForeignKey(
            User, on_delete=models.CASCADE, related_name="reports"
        ),
    )
    diagnosis = models.TextField()
    prescription = models.TextField(blank=True, null=True)
    report_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.patient.user.username} on {self.report_date}"
