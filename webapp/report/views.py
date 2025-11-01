from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Report
from report.serializers import (
    CreateReportSerializer,
    ListReportSerializer,
    RetrieveReportSerializer,
    UpdateReportSerializer,
)


class ReportCreateAPIView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = CreateReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ReportListAPIView(generics.ListAPIView):
    queryset = Report.objects.all().order_by("-report_date")
    serializer_class = ListReportSerializer
    permission_classes = [IsAuthenticated]


class ReportRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Report.objects.all()
    serializer_class = RetrieveReportSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class ReportUpdateAPIView(generics.UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = UpdateReportSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
