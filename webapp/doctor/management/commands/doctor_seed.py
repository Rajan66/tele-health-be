from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from doctor.models import Doctor
from hospital.models import Department
from gatekeeper.models import User


class Command(BaseCommand):
    help = "Seed doctors for existing departments"

    def handle(self, *args, **options):
        Doctor.objects.all().delete()
        self.stdout.write(self.style.WARNING("🗑 Cleared all existing data"))

        departments = Department.objects.select_related("hospital").all()
        if not departments.exists():
            self.stdout.write(
                self.style.ERROR(
                    "❌ No departments found! Run seed_hospitals and seed_departments first."
                )
            )
            return

        sample_doctors = [
            {"first_name": "Ramesh", "last_name": "Shrestha"},
            {"first_name": "Sita", "last_name": "Koirala"},
            {"first_name": "Bikash", "last_name": "Lama"},
            {"first_name": "Manisha", "last_name": "Thapa"},
            {"first_name": "Prakash", "last_name": "Bhandari"},
        ]

        for dept in departments:
            for doc_data in sample_doctors:
                email = f"{doc_data['first_name'].lower()}.{
                    dept.name.lower().replace(' ', '')
                }@{dept.hospital.name.lower().replace(' ', '')}.com"
                password = get_random_string(8)

                user, _ = User.objects.get_or_create(
                    email=email,
                    defaults={
                        "first_name": doc_data["first_name"],
                        "last_name": doc_data["last_name"],
                        "role": "doctor",
                        "password": password,
                    },
                )

                doctor, created = Doctor.objects.get_or_create(
                    user=user,
                    defaults={
                        "department": dept,
                        "contact": f"98{get_random_string(8, '0123456789')}",
                    },
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"✅ Created Doctor: {doctor.user.first_name} {
                                doctor.user.last_name
                            } ({dept.name} - {dept.hospital.name})"
                        )
                    )
                else:
                    self.stdout.write(
                        f"⚠️ Doctor already exists: {doctor.user.email}"
                    )

        self.stdout.write(
            self.style.SUCCESS("🎉 Doctors seeded successfully!")
        )
