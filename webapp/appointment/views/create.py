from rest_framework.generics import CreateAPIView  # noqa
from rest_framework.permissions import IsAuthenticated
from appointment.models import Appointment
from appointment.serializers import CreateAppointmentSerializer


class CreateAppointmentView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = CreateAppointmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
