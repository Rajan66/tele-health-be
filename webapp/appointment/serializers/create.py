from rest_framework import serializers
from appointment.models import Appointment
from notification.models import Notification
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
        return f"{frontend_url}?room_id={obj.room_id}"

    def create(self, validated_data):
        request = self.context["request"]

        health_worker = request.user.health_worker_profile

        # generate room id
        room_id = str(uuid.uuid4())

        appointment = Appointment.objects.create(
            health_worker=health_worker,
            **validated_data,
        )

        # set meeting link
        appointment.meeting_link = (
            f"http://localhost:3000/meeting?room_id={room_id}"
        )
        appointment.save()

        # create notification
        Notification.objects.create(
            doctor=appointment.doctor.user,
            health_worker=request.user,
            message=f"New appointment booked by {
                request.user.email
            }. Here's the meeting link: {appointment.meeting_link}",
        )

        return appointment
