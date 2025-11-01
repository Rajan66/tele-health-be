import os
import zipfile
from io import BytesIO

from django.core.files import File
from django.core.management.base import BaseCommand
from gatekeeper.models import User
from hospital.models import Hospital

# __file__ = .../webapp/hospital/management/commands/seed_hospitals.py
# We go up three directories to reach webapp/
WEBAPP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ZIP_PATH = os.path.join(WEBAPP_DIR, "Hospitals.zip")



class Command(BaseCommand):
    help = "Seed default hospitals with images from ZIP"

    def handle(self, *args, **options):
        # Clear old hospitals and hospital users
        Hospital.objects.all().delete()
        User.objects.filter(role="hospital").delete()

        hospital_data = [
            {"name": "City Hospital", "email": "cityhospital@gmail.com", "contact": "9812345678", "address": "Kathmandu", "image_name": "city_hospital.png"},
            {"name": "Metro Care Hospital", "email": "metrocare@gmail.com", "contact": "9801234567", "address": "Lalitpur", "image_name": "metro_care_hospital.jpg"},
            {"name": "Bir Hospital", "email": "birhospital@gmail.com", "contact": "9841239876", "address": "Kathmandu", "image_name": "bir_hospital.jpg"},
            {"name": "Bharosa Medical Center", "email": "bharosa@gmail.com", "contact": "9867775544", "address": "Pokhara", "image_name": "bharosa_medical_center.jpg"},
        ]

        if not os.path.exists(ZIP_PATH):
            self.stdout.write(self.style.ERROR(f"❌ ZIP file not found at {ZIP_PATH}"))
            return

        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_file:
            zip_files = zip_file.namelist()

            for data in hospital_data:
                # Create User
                user, _ = User.objects.get_or_create(
                    email=data["email"],
                    defaults={
                        "first_name": data["name"].split()[0],
                        "last_name": data["name"].split()[-1],
                        "role": "hospital",
                        "password": "admin1234",
                    },
                )

                # Create Hospital
                hospital, created = Hospital.objects.get_or_create(
                    user=user,
                    defaults={
                        "name": data["name"],
                        "contact": data["contact"],
                        "address": data["address"],
                    },
                )

                # Auto-match image from ZIP
                expected_image_name_jpg = f"{data['name'].lower().replace(' ', '_')}.jpg"
                expected_image_name_png = f"{data['name'].lower().replace(' ', '_')}.png"

                image_name = None
                if expected_image_name_jpg in zip_files:
                    image_name = expected_image_name_jpg
                elif expected_image_name_png in zip_files:
                    image_name = expected_image_name_png

                if image_name:
                    image_data = zip_file.read(image_name)
                    hospital.image.save(
                        image_name, File(BytesIO(image_data)), save=True
                    )
                    self.stdout.write(self.style.SUCCESS(f"🖼️ Added image for {hospital.name}"))
                else:
                    self.stdout.write(self.style.WARNING(f"⚠️ No image found for {hospital.name}"))

                if created:
                    self.stdout.write(self.style.SUCCESS(f"✅ Created hospital: {hospital.name}"))
                else:
                    self.stdout.write(f"⚠️ Hospital already exists: {hospital.name}")
