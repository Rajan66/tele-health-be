from django.urls import path

from hospital.views.hospital import (
    ListHospitalView,
    RetrieveHospitalView,
)

urlpatterns = [
    path(
        "list/",
        ListHospitalView.as_view(),
        name="list-hospital",
    ),
    path(
        "retrieve/<uuid:pk>/",
        RetrieveHospitalView.as_view(),
        name="create-hospital",
    ),
]
