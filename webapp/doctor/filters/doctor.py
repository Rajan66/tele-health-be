from django_filters import rest_framework as filters
from doctor.models import Doctor


class ListDoctorFilter(filters.FilterSet):
    iname = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    department = filters.UUIDFilter(
        required=False,
    )

    is_available = filters.BooleanFilter(
        required=False,
    )

    class Meta:
        model = Doctor

        fields = (
            "iname",
            "department",
            "is_available",
        )
