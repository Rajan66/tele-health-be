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
    help = "Seed ~100 doctors distributed across departments and hospitals with sequential images"

    DEFAULT_PASSWORD = "admin123"

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
        if not os.path.exists(image_dir):
            self.stdout.write(
                self.style.ERROR(f"❌ Image folder not found: {image_dir}")
            )
            return

        created_count = 0
        for i in range(1, 101):  # 100 doctors
            dept = random.choice(departments)
            first = random.choice(first_names)
            last = random.choice(last_names)
            hospital_slug = slugify(dept.hospital.name)
            email = f"{first.lower()}.{last.lower()}@{hospital_slug}.com"

            user = User.objects.create_user(
                email=email,
                password=self.DEFAULT_PASSWORD,
                first_name=first,
                last_name=last,
                role="doctor",
            )

            # Sequential image
            image_filename = f"doctor_{i}.png"
            image_path = os.path.join(image_dir, image_filename)
            if os.path.exists(image_path):
                with open(image_path, "rb") as f:
                    doctor_image = File(BytesIO(f.read()), name=image_filename)
            else:
                doctor_image = None

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
                        dept.hospital.name
                    }) - {email}"
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"🎉 Successfully seeded {created_count} doctors!"
            )
        )
