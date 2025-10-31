from django.urls import path  # noqa
from doctor.views import ListDoctorView, RetrieveDoctorView

urlpatterns = [
    path(
        "list/",
        ListDoctorView.as_view(),
        name="list-doctor",
    ),
    path(
        "retrieve/<uuid:pk>/",
        RetrieveDoctorView.as_view(),
        name="retrieve-doctor",
    ),
]
