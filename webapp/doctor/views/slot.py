from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from doctor.models import TimeSlot, Doctor
from doctor.serializers.doctor import TimeSlotSerializer


class ListDoctorTimeSlotView(ListAPIView):
    serializer_class = TimeSlotSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["is_booked"]
    queryset = TimeSlot.objects.none()

    def get_queryset(self):
        doctor_id = self.kwargs.get("doctor_id")
        doctor = get_object_or_404(Doctor, id=doctor_id)
        return TimeSlot.objects.filter(doctor=doctor).order_by("start_time")
