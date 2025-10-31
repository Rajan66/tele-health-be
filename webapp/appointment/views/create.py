from rest_framework.generics import CreateAPIView  # noqa
from appointment.models import Appointment
from appointment.serializers import CreateAppointmentSerializer


class CreateAppointmentView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = CreateAppointmentSerializer

    def perform_create(self, serializer):
        serializer.save
