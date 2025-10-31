from rest_framework.generics import RetrieveAPIView

from doctor.serializers.doctor import RetrieveDoctorSerializer


class RetrieveDoctorView(RetrieveAPIView):
    serializer_class = RetrieveDoctorSerializer
