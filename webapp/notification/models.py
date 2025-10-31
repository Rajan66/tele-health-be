from django.db import models
from base.models import BaseModel
from gatekeeper.models import User


class Notification(BaseModel):
    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="doctor_notifications",
        null=True,
        blank=True,
    )
    health_worker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="health_worker_notifications",
        null=True,
        blank=True,
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        target = (
            self.doctor.email
            if self.doctor
            else (
                self.health_worker.user.email
                if self.health_worker
                else "Unknown"
            )
        )
        return f"To {target}: {self.message[:30]}"
