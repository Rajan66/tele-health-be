from django_filters import rest_framework as filters
from hospital.models import Hospital


class ListHospitalFilter(filters.FilterSet):
    iname = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = Hospital

        fields = ("iname",)
