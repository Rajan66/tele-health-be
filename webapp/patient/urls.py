from django.urls import path  # noqa
from doctor.views import (
    CreatePatientView,
    ListPatientView,
    RetrievePatientView,
)

urlpatterns = [
    path(
        "create/",
        CreatePatientView.as_view(),
        name="create-patient",
    ),
    path(
        "retrieve/<uuid:pk>/",
        RetrievePatientView.as_view(),
        name="retrieve-patient",
    ),
    path(
        "<uuid:doctor_id>/slots/",
        ListPatientView.as_view(),
        name="list-patient",
    ),
]
