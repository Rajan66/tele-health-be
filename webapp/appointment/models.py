from base.models import BaseModel  # noqa

from django.db import models

from doctor.models import Doctor
from worker.models import HealthWorker
from hospital.models import Hospital


class Appointment(BaseModel):
    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="appointments"
    )
    health_worker = models.ForeignKey(
        HealthWorker, on_delete=models.CASCADE, related_name="appointments"
    )
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="appointments"
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="scheduled"
    )
    meeting_link = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.doctor} with {self.health_worker} at {self.start_time.strftime('%Y-%m-%d %H:%M')}"  # noqa
