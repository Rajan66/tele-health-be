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
    help = "Seed 2-3 reports per patient, ensuring each doctor has at least one report"

    def handle(self, *args, **options):
        # Clear existing reports
        Report.objects.all().delete()

        patients = list(Patient.objects.all())
        doctors = list(Doctor.objects.all())
        users = list(User.objects.all())  # for created_by

        if not patients or not users or not doctors:
            self.stdout.write(
                self.style.ERROR("Seed patients, users, and doctors first.")
            )
            return

        # Track doctors that have been assigned at least once
        assigned_doctors = set()

        for patient in patients:
            report_count = random.randint(2, 3)
            for _ in range(report_count):
                # Assign a doctor
                if len(assigned_doctors) < len(doctors):
                    # Ensure each doctor gets at least one report
                    available_doctors = [
                        d for d in doctors if d.id not in assigned_doctors
                    ]
                    doctor = random.choice(available_doctors)
                    assigned_doctors.add(doctor.id)
                else:
                    doctor = random.choice(doctors)

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
                            patient.last_name
                        } "
                        f"by {created_by.email} with doctor {
                            doctor.user.email
                        }"
                    )
                )
