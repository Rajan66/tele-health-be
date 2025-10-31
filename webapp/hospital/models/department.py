from django.db import models  # noqa

from base.models import BaseModel

from hospital.models.hospital import Hospital


class Department(BaseModel):
    name = models.CharField(max_length=100)
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="departments"
    )

    def __str__(self):
        return f"{self.name} ({self.hospital.name})"
