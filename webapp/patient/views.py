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
        serializer.save(created_by=self.request.user)


class ListPatientView(generics.ListAPIView):
    serializer_class = ListPatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Patient.objects.all()
        if user.role == "doctor":
            return Patient.objects.all().reverse()
        return Patient.objects.filter(created_by=user)


class RetrievePatientView(generics.RetrieveAPIView):
    serializer_class = RetrievePatientSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return Patient.objects.filter(created_by=user)
