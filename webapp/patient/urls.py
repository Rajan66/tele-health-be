from django.urls import path  # noqa
from patient.views import (
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
        "list",
        ListPatientView.as_view(),
        name="list-patient",
    ),
    path(
        "retrieve/<uuid:pk>/",
        RetrievePatientView.as_view(),
        name="retrieve-patient",
    ),
]
