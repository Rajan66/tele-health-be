from rest_framework import serializers  # noqa
from appointment.models import Appointment


class ListAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
