from rest_framework import serializers  # noqa
from appointment.models import Appointment
from notification.models import Notification


class CreateAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ["status", "created_at", "health_worker"]

    def create(self, validated_data):
        request = self.context["request"]
        health_worker = request.user.healthworker
        time_slot = validated_data["time_slot"]

        # 1️⃣ Mark the time slot as booked
        if time_slot.is_booked:
            raise serializers.ValidationError(
                "This time slot is already booked."
            )
        time_slot.is_booked = True
        time_slot.save()

        # 2️⃣ Create appointment
        appointment = Appointment.objects.create(
            health_worker=health_worker, **validated_data
        )

        # 3️⃣ Send notification to the doctor
        Notification.objects.create(
            user=appointment.doctor.user,
            message=f"New appointment booked by {
                health_worker.user.email
            } for {time_slot.start_time}.",
        )

        return appointment
