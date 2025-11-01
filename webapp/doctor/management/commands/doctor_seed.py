import random
import os
from io import BytesIO
from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.conf import settings

from gatekeeper.models import User
from doctor.models import Doctor
from hospital.models import Department


class Command(BaseCommand):
    help = "Seed doctors per department per hospital (max 300 total)"

    DEFAULT_PASSWORD = "admin123"
    MAX_DOCTORS = 300

    def handle(self, *args, **options):
        # Clear old doctors & users
        Doctor.objects.all().delete()
        User.objects.filter(role="doctor").delete()
        self.stdout.write(
            self.style.WARNING("🗑 Cleared existing doctors and users")
        )

        departments = Department.objects.select_related("hospital").all()
        if not departments.exists():
            self.stdout.write(
                self.style.ERROR(
                    "❌ No departments found! Seed hospitals & departments first."
                )
            )
            return

        first_names = [
            "Ramesh",
            "Sita",
            "Bikash",
            "Manisha",
            "Prakash",
            "Sunita",
            "Kiran",
            "Nirmala",
            "Dipesh",
            "Laxmi",
            "Bishal",
            "Sarita",
            "Rajesh",
            "Anita",
            "Suman",
            "Pushpa",
            "Roshan",
            "Bhawana",
            "Raju",
            "Rekha",
            "Dinesh",
            "Keshav",
            "Puja",
            "Kamal",
            "Asha",
            "Narayan",
            "Sanjay",
            "Mina",
            "Buddhi",
            "Krishna",
        ]
        last_names = [
            "Shrestha",
            "Koirala",
            "Lama",
            "Thapa",
            "Bhandari",
            "KC",
            "Adhikari",
            "Maharjan",
            "Basnet",
            "Rai",
            "Tamang",
            "Gurung",
            "Bhattarai",
            "Poudel",
            "Nepal",
            "Dahal",
            "Pandey",
            "Shah",
            "Karki",
            "Malla",
        ]

        image_dir = os.path.join(settings.BASE_DIR, "doctor_images")
        image_files = sorted(
            [
                os.path.join(image_dir, f)
                for f in os.listdir(image_dir)
                if f.lower().endswith((".jpg", ".jpeg", ".png"))
            ]
        )

        if not os.path.exists(image_dir) or not image_files:
            self.stdout.write(
                self.style.WARNING(
                    "⚠️ Doctor images missing, will create without images."
                )
            )
            image_files = []

        email_counter = {}  # To avoid duplicate emails
        created_count = 0
        image_index = 0

        for dept in departments:
            if created_count >= self.MAX_DOCTORS:
                break

            num_doctors = random.randint(1, 5)  # assign 1-5 doctors per dept
            for _ in range(num_doctors):
                if created_count >= self.MAX_DOCTORS:
                    break

                first = random.choice(first_names)
                last = random.choice(last_names)
                hospital_slug = slugify(dept.hospital.name)

                base_email = (
                    f"{first.lower()}.{last.lower()}@{hospital_slug}.com"
                )
                count = email_counter.get(base_email, 0)
                email_counter[base_email] = count + 1
                email = (
                    base_email
                    if count == 0
                    else f"{first.lower()}.{last.lower()}{count}@{hospital_slug}.com"
                )

                user = User.objects.create_user(
                    email=email,
                    password=self.DEFAULT_PASSWORD,
                    first_name=first,
                    last_name=last,
                    role="doctor",
                )

                doctor_image = None
                if image_files:
                    image_path = image_files[image_index % len(image_files)]
                    image_index += 1
                    with open(image_path, "rb") as f:
                        doctor_image = File(
                            BytesIO(f.read()),
                            name=os.path.basename(image_path),
                        )

                Doctor.objects.create(
                    user=user,
                    department=dept,
                    contact=f"98{random.randint(10000000, 99999999)}",
                    experience_years=random.randint(1, 20),
                    is_available=random.choice([True, True, False]),
                    image=doctor_image,
                )

                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"✅ Dr. {first} {last} ({dept.name}, {
                            dept.hospital.name}) - {email}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"🎉 Successfully seeded {created_count} doctors!"
            )
        )
