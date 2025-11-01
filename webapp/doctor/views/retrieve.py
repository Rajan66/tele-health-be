from rest_framework.generics import RetrieveAPIView  # noqa

from doctor.serializers.doctor import RetrieveDoctorSerializer
from doctor.models import Doctor


class RetrieveDoctorView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = RetrieveDoctorSerializer
