import os
from io import BytesIO

from django.core.files import File
from django.core.management.base import BaseCommand
from gatekeeper.models import User
from hospital.models import Hospital


class Command(BaseCommand):
    help = (
        "Seed 10 government hospitals with images from webapp/hospital_images/"
    )

    def handle(self, *args, **options):
        # 🔹 Path setup
        BASE_DIR = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../..")
        )
        IMAGE_DIR = os.path.join(BASE_DIR, "hospital_images")

        if not os.path.exists(IMAGE_DIR):
            self.stdout.write(
                self.style.ERROR(f"❌ Image folder not found: {IMAGE_DIR}")
            )
            return

        # 🔹 Wipe old data
        Hospital.objects.all().delete()
        User.objects.filter(role="hospital").delete()
        self.stdout.write(
            self.style.WARNING("🗑️ Cleared old hospitals and hospital users")
        )

        # 🔹 List of 10 government hospitals
        hospitals = [
            {
                "name": "APF Hospital Balambu",
                "email": "apfbalambu@gmail.com",
                "contact": "9811111111",
                "address": "Balambu, Kathmandu",
                "image": "apf_hospital_balambu.jpg",
            },
            {
                "name": "Bir Hospital",
                "email": "birhospital@gmail.com",
                "contact": "9811111112",
                "address": "Kathmandu",
                "image": "bir hospital.jpg",
            },
            {
                "name": "Civil Hospital",
                "email": "civilhospital@gmail.com",
                "contact": "9811111113",
                "address": "Kathmandu",
                "image": "civil.png",
            },
            {
                "name": "Narayani Provincial Hospital",
                "email": "narayani@gmail.com",
                "contact": "9811111114",
                "address": "Birgunj",
                "image": "narayani_provincal_hospital.jpg",
            },
            {
                "name": "Palpa Hospital",
                "email": "palpahospital@gmail.com",
                "contact": "9811111115",
                "address": "Palpa",
                "image": "palpa_hospital.jpg",
            },
            {
                "name": "Paropakar Maternity and Women Hospital",
                "email": "paropakar@gmail.com",
                "contact": "9811111116",
                "address": "Thapathali, Kathmandu",
                "image": "paropakar_maternity_and_women hospital.JPG",
            },
            {
                "name": "Pashupati Homeopathic Hospital",
                "email": "pashupatihomeo@gmail.com",
                "contact": "9811111117",
                "address": "Gaushala, Kathmandu",
                "image": "pashupati_homeopathic_hospital.jpg",
            },
            {
                "name": "Patan Academy of Health Science",
                "email": "patanacademy@gmail.com",
                "contact": "9811111118",
                "address": "Lalitpur",
                "image": "patan_academic_of_health_science.jpg",
            },
            {
                "name": "Shahid Gangalal National Heart Center",
                "email": "gangalalheart@gmail.com",
                "contact": "9811111119",
                "address": "Bansbari, Kathmandu",
                "image": "shadhi_gangalal_national_heart_center.jpg",
            },
            {
                "name": "Tri Chandra Military Hospital",
                "email": "trichandra@gmail.com",
                "contact": "9811111120",
                "address": "Kathmandu",
                "image": "tri_chandra_military.jpg",
            },
        ]

        for data in hospitals:
            # Create user
            user = User.objects.create_user(
                email=data["email"],
                password="admin1234",
                first_name=data["name"].split()[0],
                last_name=data["name"].split()[-1],
                role="hospital",
            )

            # Create hospital
            hospital = Hospital.objects.create(
                user=user,
                name=data["name"],
                contact=data["contact"],
                address=data["address"],
            )

            # Add image
            image_path = os.path.join(IMAGE_DIR, data["image"])
            if os.path.exists(image_path):
                with open(image_path, "rb") as f:
                    hospital.image.save(
                        os.path.basename(image_path),
                        File(BytesIO(f.read())),
                        save=True,
                    )
                self.stdout.write(
                    self.style.SUCCESS(f"🖼️ Added image for {hospital.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"⚠️ Image not found: {data['image']}")
                )

        self.stdout.write(
            self.style.SUCCESS(
                "✅ Successfully seeded 10 government hospitals!"
            )
        )
