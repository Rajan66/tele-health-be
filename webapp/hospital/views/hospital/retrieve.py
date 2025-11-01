from rest_framework.generics import RetrieveAPIView

from hospital.serializers.hospital import RetrieveHospitalSerializer


class RetrieveHospitalView(RetrieveAPIView):
    serializer_class = RetrieveHospitalSerializer
