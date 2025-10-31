from datetime import datetime, date, time, timedelta
from django.core.management.base import BaseCommand
from doctor.models import Doctor, TimeSlot


class Command(BaseCommand):
    help = "Seed time slots for all doctors for the next 30 days"

    def handle(self, *args, **options):
        TimeSlot.objects.all().delete()
        self.stdout.write(self.style.WARNING("🗑 Cleared all existing data"))

        # Define standard slot durations (30 minutes each)
        slot_durations = [
            (time(9, 0), time(9, 30)),
            (time(9, 30), time(10, 0)),
            (time(10, 0), time(10, 30)),
            (time(10, 30), time(11, 0)),
            (time(11, 0), time(11, 30)),
            (time(11, 30), time(12, 0)),
            (time(13, 0), time(13, 30)),
            (time(13, 30), time(14, 0)),
            (time(14, 0), time(14, 30)),
            (time(14, 30), time(15, 0)),
            (time(15, 0), time(15, 30)),
            (time(15, 30), time(16, 0)),
        ]

        doctors = Doctor.objects.all()
        if not doctors.exists():
            self.stdout.write(
                self.style.ERROR("❌ No doctors found! Seed doctors first.")
            )
            return

        today = date.today()
        days_to_seed = 7

        for doctor in doctors:
            for day_offset in range(days_to_seed):
                current_day = today + timedelta(days=day_offset)
                for start, end in slot_durations:
                    start_dt = datetime.combine(current_day, start)
                    end_dt = datetime.combine(current_day, end)

                    TimeSlot.objects.get_or_create(
                        doctor=doctor,
                        start_time=start_dt,
                        end_time=end_dt,
                    )

            self.stdout.write(
                self.style.SUCCESS(
                    f"✅ Slots created for {doctor.user.email} for 7 days"
                )
            )

        self.stdout.write(
            self.style.SUCCESS("🎉 All time slots seeded successfully!")
        )
