from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from report.models import Report
from report.serializers import (
    CreateReportSerializer,
    ListReportSerializer,
    RetrieveReportSerializer,
)


class ReportCreateAPIView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = CreateReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Save the logged-in user as creator
        serializer.save(created_by=self.request.user)


class ReportListAPIView(generics.ListAPIView):
    serializer_class = ListReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, "doctor_profile"):
            return Report.objects.filter(doctor=user.doctor_profile).order_by(
                "-report_date"
            )
        elif hasattr(user, "health_worker_profile"):
            return Report.objects.filter(created_by=user).order_by(
                "-report_date"
            )
        return Report.objects.none()


class ReportRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = RetrieveReportSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "patient_id"

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, "doctor_profile"):
            return Report.objects.filter(doctor=user.doctor_profile)
        elif hasattr(user, "health_worker_profile"):
            return Report.objects.filter(created_by=user)
        return Report.objects.none()
