from django.shortcuts import render

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
    queryset = Patient.objects.all()
    serializer_class = ListPatientSerializer
    permission_classes = [IsAuthenticated]


class RetrieveAPIView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = RetrievePatientSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
