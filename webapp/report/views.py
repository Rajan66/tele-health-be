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
    serializer_class = ListReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, "doctor_profile"):
            return Report.objects.filter(doctor=user.doctor_profile).order_by(
                "-report_date"
            )
        elif hasattr(user, "health_worker_profile"):
            return Report.objects.filter(
                patient__health_worker=user.health_worker_profile
            ).order_by("-report_date")
        return Report.objects.none()


class ReportRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = RetrieveReportSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "patient_id"

    def get_object(self):
        user = self.request.user
        patient_id = self.kwargs.get(self.lookup_field)

        queryset = Report.objects.none()

        if hasattr(user, "doctor_profile"):
            queryset = Report.objects.filter(doctor=user.doctor_profile)
        elif hasattr(user, "health_worker_profile"):
            queryset = Report.objects.filter(
                patient__health_worker=user.health_worker_profile
            )

        # Filter by patient_id
        obj = generics.get_object_or_404(queryset, patient_id=patient_id)
        return obj


class ReportUpdateAPIView(generics.UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = UpdateReportSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
