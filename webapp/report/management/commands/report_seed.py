import random
from django.core.management.base import BaseCommand
from report.models import Report
from patient.models import Patient
from doctor.models import Doctor
from gatekeeper.models import User

diagnoses = [
    "Flu-like symptoms",
    "High blood pressure",
    "Diabetes Type 2",
    "Migraine",
    "Allergic reaction",
    "Stomach infection",
    "Fracture",
    "Asthma attack",
]

prescriptions = [
    "Paracetamol 500mg twice daily",
    "Ibuprofen 400mg as needed",
    "Insulin injection daily",
    "Antihistamines once a day",
    "Rest and hydration",
    "Antibiotics for 7 days",
    "Physical therapy",
    "Inhaler as needed",
]


class Command(BaseCommand):
    help = "Seed reports"

    def handle(self, *args, **options):
        Report.objects.all().delete()

        patients = list(Patient.objects.all())
        doctors = list(Doctor.objects.all())
        users = list(User.objects.all())  # for created_by

        if not patients or not users:
            self.stdout.write(
                self.style.ERROR(
                    "No patients or users found. Seed them first."
                )
            )
            return

        for _ in range(30):  # create 30 reports
            patient = random.choice(patients)
            doctor = random.choice(doctors) if doctors else None
            created_by = random.choice(users)

            report = Report.objects.create(
                patient=patient,
                doctor=doctor,
                created_by=created_by,
                diagnosis=random.choice(diagnoses),
                prescription=random.choice(prescriptions),
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Created report for {patient.first_name} {
                        patient.last_name} by {created_by.email}"
                )
            )
