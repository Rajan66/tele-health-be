from rest_framework.generics import ListAPIView  # noqa
from django_filters.rest_framework import DjangoFilterBackend

from doctor.serializers.doctor import ListDoctorSerializer
from doctor.filters.doctor import ListDoctorFilter
from doctor.models import Doctor


class ListDoctorView(ListAPIView):
    queryset = Doctor.objects.all()

    serializer_class = ListDoctorSerializer

    filterset_class = ListDoctorFilter

    filter_backends = [DjangoFilterBackend]
