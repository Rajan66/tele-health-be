from doctor.views.list import (  # noqa
    ListDoctorView,
)
from doctor.views.retrieve import RetrieveDoctorView
from doctor.views.slot import ListDoctorTimeSlotView

__all__ = [
    "ListDoctorView",
    "RetrieveDoctorView",
    "ListDoctorTimeSlotView",
]
