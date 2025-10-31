# management/commands/seed_healthworkers.py
from django.core.management.base import BaseCommand
from gatekeeper.models import User
from worker.models import HealthWorker
import random


class Command(BaseCommand):
    help = "Seed 20 sample health workers in village areas"

    def handle(self, *args, **options):
        # 1️⃣ Delete existing health workers and their users
        health_workers = HealthWorker.objects.all()
        for hw in health_workers:
            if hw.user:
                hw.user.delete()  # Deletes both User and cascades HealthWorker
        self.stdout.write(
            self.style.SUCCESS(
                "🗑 Deleted all existing health workers and users."
            )
        )

        # 2️⃣ Seed new health workers
        first_names = [
            "Sita",
            "Ram",
            "Hari",
            "Gita",
            "Anil",
            "Mina",
            "Bikash",
            "Rekha",
            "Kiran",
            "Laxmi",
            "Santosh",
            "Pooja",
            "Ramesh",
            "Suman",
            "Nisha",
            "Prakash",
            "Sujata",
            "Manoj",
            "Asha",
            "Binod",
        ]
        last_name = "HealthWorker"
        village_areas = [
            "Tistung",
            "Dhading",
            "Dapcha",
            "Sundarijal",
            "Chitlang",
            "Pharping",
            "Banepa",
            "Panauti",
            "Lamosangu",
            "Kavre",
        ]

        for i in range(20):
            email = f"hw{i + 1}@example.com"
            first_name = first_names[i]
            area = random.choice(village_areas)
            user = User.objects.create(
                email=email,
                role="health_worker",
                first_name=first_name,
                last_name=last_name,
            )
            # Set password (optional: hashed using set_password)
            user.set_password("defaultpassword123")
            user.save()

            health_worker = HealthWorker.objects.create(
                user=user,
                contact=f"98000000{i + 1:02}",
                area=area,
            )
            self.stdout.write(
                self.style.SUCCESS(f"✅ Created {user.email} in {area}")
            )

        self.stdout.write(
            self.style.SUCCESS("🎉 20 Health workers seeded successfully!")
        )
