from django.core.management.base import BaseCommand  # noqa
from hospital.models import Hospital
from gatekeeper.models import User


class Command(BaseCommand):
    help = "Seed default hospitals"

    def handle(self, *args, **options):
        Hospital.objects.all().delete()
        hospital_data = [
            {
                "name": "City Hospital",
                "email": "cityhospital@gmail.com",
                "contact": "9812345678",
                "address": "Kathmandu",
            },
            {
                "name": "Metro Care Hospital",
                "email": "metrocare@gmail.com",
                "contact": "9801234567",
                "address": "Lalitpur",
            },
            {
                "name": "Bir Hospital",
                "email": "birhospital@gmail.com",
                "contact": "9841239876",
                "address": "Kathmandu",
            },
            {
                "name": "Bharosa Medical Center",
                "email": "bharosa@gmail.com",
                "contact": "9867775544",
                "address": "Pokhara",
            },
        ]

        for data in hospital_data:
            # create hospital user first
            user, _ = User.objects.get_or_create(
                email=data["email"],
                defaults={
                    "first_name": data["name"].split()[0],
                    "last_name": data["name"].split()[-1],
                    "role": "hospital",
                    "password": "admin1234",  # you can later reset these
                },
            )

            hospital, created = Hospital.objects.get_or_create(
                user=user,
                defaults={
                    "name": data["name"],
                    "contact": data["contact"],
                    "address": data["address"],
                },
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"✅ Created hospital: {hospital.name}")
                )
            else:
                self.stdout.write(
                    f"⚠️ Hospital already exists: {hospital.name}"
                )
