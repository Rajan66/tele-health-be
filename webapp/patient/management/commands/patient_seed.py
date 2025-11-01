import random
from django.core.management.base import BaseCommand
from patient.models import Patient

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
    help = "Seed patients with village addresses"

    def handle(self, *args, **options):
        # Clear existing patients
        Patient.objects.all().delete()

        for _ in range(20):  # create 20 patients
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
                address=random.choice(villages),  # pick a random village
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Created patient: {patient.first_name} {
                        patient.last_name} ({patient.address})"
                )
            )
