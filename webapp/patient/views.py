from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from .serializers import (
    CreatePatientSerializer,
    ListPatientSerializer,
    RetrievePatientSerializer,
)


class CreatePatientView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = CreatePatientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ListPatientView(generics.ListAPIView):
    serializer_class = ListPatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, "doctor_profile"):
            return Patient.objects.filter(doctor=user.doctor_profile)
        elif hasattr(user, "health_worker_profile"):
            return Patient.objects.filter(
                health_worker=user.health_worker_profile
            )
        return Patient.objects.none()


class RetrievePatientView(generics.RetrieveAPIView):
    serializer_class = RetrievePatientSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, "doctor_profile"):
            return Patient.objects.filter(doctor=user.doctor_profile)
        elif hasattr(user, "health_worker_profile"):
            return Patient.objects.filter(
                health_worker=user.health_worker_profile
            )
        return Patient.objects.none()
