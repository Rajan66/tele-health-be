from rest_framework import serializers
from appointment.models import Appointment
from notification.models import Notification
from doctor.models import TimeSlot
import uuid


class CreateAppointmentSerializer(serializers.ModelSerializer):
    meeting_link = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Appointment
        fields = [
            "id",
            "doctor",
            "health_worker",
            "start_time",
            "end_time",
            "status",
            "meeting_link",
            "notes",
        ]
        read_only_fields = [
            "status",
            "health_worker",
            "meeting_link",
        ]

    def get_meeting_link(self, obj):
        if not getattr(obj, "room_id", None):
            return None
        frontend_url = "http://localhost:3000/meeting"
        return f"{frontend_url}/{obj.room_id}"

    def create(self, validated_data):
        request = self.context["request"]
        health_worker = request.user.health_worker_profile

        room_id = str(uuid.uuid4())

        appointment = Appointment.objects.create(
            health_worker=health_worker,
            **validated_data,
        )

        doctor = appointment.doctor
        start_time = appointment.start_time

        try:
            slot = TimeSlot.objects.get(
                doctor=doctor, start_time=start_time, is_booked=False
            )
            slot.is_booked = True
            slot.save()
        except TimeSlot.DoesNotExist:
            pass

        formatted_str = start_time.strftime("%b %d, %I:%M%p").lower()

        Notification.objects.create(
            doctor=doctor.user,
            health_worker=request.user,
            message=f"New appointment booked by {request.user.email} for {formatted_str}.",  # noqa
            meeting_link=appointment.meeting_link,
        )

        return appointment
