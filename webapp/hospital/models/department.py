from django.db import models

from hospital.models.hospital import Hospital


class Department(models.Model):
    name = models.CharField(max_length=100)
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="departments"
    )

    def __str__(self):
        return f"{self.name} ({self.hospital.name})"
