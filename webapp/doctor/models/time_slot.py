from django.db import models  # noqa
from base.models import BaseModel
from doctor.models.doctor import Doctor


class TimeSlot(BaseModel):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="slots"
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doctor} - {self.start_time.strftime('%H:%M')}"
