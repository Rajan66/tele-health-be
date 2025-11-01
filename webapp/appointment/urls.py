from django.urls import path  # noqa
from appointment.views import ListAppointmentView, CreateAppointmentView

urlpatterns = [
    path("list/", ListAppointmentView.as_view(), name="list-appointment"),
    path(
        "create/",
        CreateAppointmentView.as_view(),
        name="create-appointment",
    ),
]
