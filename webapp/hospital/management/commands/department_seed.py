from django.core.management.base import BaseCommand  # noqa
from hospital.models import (
    Department,
    Hospital,
)


class Command(BaseCommand):
    help = "Seed departments for all hospitals"

    def handle(self, *args, **options):
        departments = [
            "General Medicine",
            "Pediatrics",
            "Gynecology",
            "Dentistry",
            "Orthopedics",
            "Cardiology",
            "Dermatology",
            "Neurology",
            "Psychiatry",
            "ENT",
        ]

        hospitals = Hospital.objects.all()
        if not hospitals.exists():
            self.stdout.write(
                self.style.ERROR(
                    "❌ No hospitals found! Please create hospitals first."
                )
            )
            return

        for hospital in hospitals:
            for dept_name in departments:
                Department.objects.get_or_create(
                    name=dept_name, hospital=hospital
                )

        self.stdout.write(
            self.style.SUCCESS(
                "✅ Departments seeded successfully for all hospitals!"
            )
        )
