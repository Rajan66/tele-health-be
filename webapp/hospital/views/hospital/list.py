from rest_framework.generics import ListAPIView  # noqa
from django_filters.rest_framework import DjangoFilterBackend

from hospital.serializers.hospital import ListHospitalSerializer
from hospital.filters.hospital import ListHospitalFilter
from hospital.models import Hospital


class ListHospitalView(ListAPIView):
    queryset = Hospital.objects.all()

    serializer_class = ListHospitalSerializer

    filterset_class = ListHospitalFilter

    filter_backends = [DjangoFilterBackend]
