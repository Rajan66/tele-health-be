from django.urls import path  # noqa
from .views import (
    ReportCreateAPIView,
    ReportListAPIView,
    ReportRetrieveAPIView,
    ReportUpdateAPIView,
)

urlpatterns = [
    path("create/", ReportCreateAPIView.as_view(), name="report-create"),
    path("list/", ReportListAPIView.as_view(), name="report-list"),
    path(
        "retrieve/<uuid:patient_id>/",
        ReportRetrieveAPIView.as_view(),
        name="report-retrieve",
    ),
    path(
        "<uuid:pk>/update/",
        ReportUpdateAPIView.as_view(),
        name="report-update",
    ),
]
