# management/commands/seed_doctors.py
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from gatekeeper.models import User
from doctor.models import Doctor
from hospital.models import Department


class Command(BaseCommand):
    help = "Seed doctors for every existing department (default password)"
    DEFAULT_PASSWORD = "admin123"  # <-- change in prod if you want

    def handle(self, *args, **options):
        # --------------------------------------------------------------
        # 1. Clean old data
        # --------------------------------------------------------------
        Doctor.objects.all().delete()  # cascades → User is deleted too
        self.stdout.write(
            self.style.WARNING(
                "Cleared all existing doctors (and their users)"
            )
        )

        # --------------------------------------------------------------
        # 2. Make sure we have departments
        # --------------------------------------------------------------
        departments = Department.objects.select_related("hospital").all()
        if not departments.exists():
            self.stdout.write(
                self.style.ERROR(
                    "No departments found! Run `seed_hospitals` and "
                    "`seed_departments` first."
                )
            )
            return

        # --------------------------------------------------------------
        # 3. Sample doctor names
        # --------------------------------------------------------------
        sample_doctors = [
            {"first_name": "Ramesh", "last_name": "Shrestha"},
            {"first_name": "Sita", "last_name": "Koirala"},
            {"first_name": "Bikash", "last_name": "Lama"},
            {"first_name": "Manisha", "last_name": "Thapa"},
            {"first_name": "Prakash", "last_name": "Bhandari"},
        ]

        # --------------------------------------------------------------
        # 4. Create doctors
        # --------------------------------------------------------------
        created_count = 0
        for dept in departments:
            hospital_slug = slugify(dept.hospital.name)
            dept_slug = slugify(dept.name)

            for doc in sample_doctors:
                # ---- e-mail -------------------------------------------------
                email = (
                    f"{doc['first_name'].lower()}.{dept_slug}"
                    f"@{hospital_slug}.com"
                )

                # ---- User (hashed password) --------------------------------
                user = User.objects.create_user(
                    email=email,
                    password=self.DEFAULT_PASSWORD,
                    first_name=doc["first_name"],
                    last_name=doc["last_name"],
                    role="doctor",
                )

                # ---- Doctor profile ----------------------------------------
                Doctor.objects.create(
                    user=user,
                    department=dept,
                    contact="9800000000",  # you can randomise later
                    experience_years=0,
                    is_available=True,
                )

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created Dr. {user.get_full_name()} "
                        f"({dept.name} – {dept.hospital.name}) | "
                        f"Login: {email} / {self.DEFAULT_PASSWORD}"
                    )
                )
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Doctors seeded successfully! ({created_count} created)"
            )
        )
