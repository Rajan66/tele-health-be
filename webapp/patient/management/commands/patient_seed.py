import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from patient.models import Patient

User = get_user_model()

first_names = ["Aarav", "Maya", "Rohan", "Sita", "Kiran", "Gita"]
last_names = ["Shrestha", "Maharjan", "Thapa", "Adhikari", "Rai", "Koirala"]
genders = ["Male", "Female", "Other"]
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
villages = [
    "Kathmandu",
    "Lalitpur",
    "Bhaktapur",
    "Pokhara",
    "Chitwan",
    "Biratnagar",
    "Dharan",
    "Butwal",
    "Hetauda",
    "Janakpur",
]


class Command(BaseCommand):
    help = "Seed patients (created by health workers only)"

    def handle(self, *args, **options):
        # Clear existing patients
        Patient.objects.all().delete()

        # Get all health worker users
        health_workers = User.objects.filter(role="health_worker")
        if not health_workers.exists():
            self.stdout.write(
                self.style.ERROR(
                    "❌ No health workers found. Please seed them first."
                )
            )
            return

        for _ in range(20):  # create 20 patients
            creator = random.choice(health_workers)
            patient = Patient.objects.create(
                first_name=random.choice(first_names),
                last_name=random.choice(last_names),
                phone=f"98{random.randint(10000000, 99999999)}",
                age=random.randint(1, 90),
                gender=random.choice(genders),
                blood_group=random.choice(blood_groups),
                weight=round(random.uniform(40, 100), 1),
                blood_pressure=f"{random.randint(
                    90, 140)}/{random.randint(60, 90)}",
                address=random.choice(villages),
                created_by=creator,
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f"✅ Created patient: {patient.first_name} {
                        patient.last_name} "
                    f"({patient.address}) by {creator.email}"
                )
            )
