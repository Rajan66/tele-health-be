from django_filters import rest_framework as filters
from doctor.models import Doctor


class ListDoctorFilter(filters.FilterSet):
    iname = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = Doctor

        fields = ("iname",)
