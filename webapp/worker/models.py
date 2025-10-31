from base.models import BaseModel  # noqa

from django.db import models


from gatekeeper.models import User


class HealthWorker(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="health_worker_profile"
    )
    contact = models.CharField(max_length=20, blank=True)
    area = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.get_full_name()
