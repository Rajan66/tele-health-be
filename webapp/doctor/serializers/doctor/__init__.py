from doctor.serializers.doctor.list import (  # noqa
    ListDoctorSerializer,
)

from doctor.serializers.doctor.retrieve import (
    RetrieveDoctorSerializer,
    RetrieveNanoDoctorSerializer,
)

from doctor.serializers.doctor.slot import TimeSlotSerializer

__all__ = [
    "ListDoctorSerializer",
    "RetrieveDoctorSerializer",
    "TimeSlotSerializer",
    "RetrieveNanoDoctorSerializer",
]
