import os
from io import BytesIO
from django.core.files import File
from django.core.management.base import BaseCommand
from hospital.models import Department, Hospital


class Command(BaseCommand):
    help = "Seed departments for all hospitals with images from department_images/ (total 100)"

    TOTAL_DEPARTMENTS = 100  # total across all hospitals

    def handle(self, *args, **options):
        BASE_DIR = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../..")
        )
        IMAGE_DIR = os.path.join(BASE_DIR, "department_images")

        if not os.path.exists(IMAGE_DIR):
            self.stdout.write(
                self.style.ERROR(f"❌ Image folder not found: {IMAGE_DIR}")
            )
            return

        # Clear existing departments
        if Department.objects.exists():
            Department.objects.all().delete()
            self.stdout.write(
                self.style.WARNING("🗑️ Cleared all existing departments")
            )
        else:
            self.stdout.write(
                "ℹ️ No existing departments found, continuing...")

        hospitals = Hospital.objects.all()
        if not hospitals.exists():
            self.stdout.write(
                self.style.ERROR(
                    "❌ No hospitals found! Please seed hospitals first."
                )
            )
            return

        # Collect image files
        image_files = [
            os.path.join(IMAGE_DIR, f)
            for f in os.listdir(IMAGE_DIR)
            if not f.startswith(".")
            and os.path.isfile(os.path.join(IMAGE_DIR, f))
        ]

        if not image_files:
            self.stdout.write(
                self.style.ERROR(
                    "❌ No department images found in department_images/"
                )
            )
            return

        # Determine how many departments per hospital
        num_hospitals = hospitals.count()
        per_hospital = self.TOTAL_DEPARTMENTS // num_hospitals
        extra = self.TOTAL_DEPARTMENTS % num_hospitals

        created_count = 0
        for i, hospital in enumerate(hospitals):
            count_for_this_hospital = per_hospital + (1 if i < extra else 0)

            for j in range(count_for_this_hospital):
                image_path = image_files[
                    (created_count + j) % len(image_files)
                ]
                dept_name = (
                    os.path.splitext(os.path.basename(image_path))[0]
                    .replace("_", " ")
                    .title()
                )

                dept = Department.objects.create(
                    name=dept_name,
                    hospital=hospital,
                )

                with open(image_path, "rb") as f:
                    dept.image.save(
                        os.path.basename(image_path),
                        File(BytesIO(f.read())),
                        save=True,
                    )

                self.stdout.write(
                    self.style.SUCCESS(
                        f"🏥 Created '{dept_name}' for {hospital.name}"
                    )
                )

            created_count += count_for_this_hospital

        self.stdout.write(
            self.style.SUCCESS(
                f"✅ Total of {created_count} departments seeded across {
                    num_hospitals} hospitals!"
            )
        )
