from rest_framework.generics import ListAPIView  # noqa
from appointment.models import Appointment
from appointment.serializers import CreateAppointmentSerializer


class ListAppointmentView(ListAPIView):
    serializer_class = CreateAppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == "doctor":
            return Appointment.objects.filter(doctor__user=user)
        elif user.role == "health_worker":
            return Appointment.objects.filter(health_worker__user=user)
        return Appointment.objects.none()
