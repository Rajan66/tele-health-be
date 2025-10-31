from base.models import BaseModel  # noqa

from django.db import models

from gatekeeper.models import User


class Hospital(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="hospital_profile"
    )
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="hospital_images/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
