from rest_framework import serializers
from doctor.models import TimeSlot


class TimeSlotSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(
        source="doctor.user.get_full_name", read_only=True
    )

    class Meta:
        model = TimeSlot
        fields = ["id", "doctor_name", "start_time", "end_time", "is_booked"]
