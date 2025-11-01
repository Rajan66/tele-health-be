from rest_framework import serializers

from hospital.models import Department
from hospital.serializers.hospital import RetrieveHospitalSerializer


class RetrieveDepartmentSerializer(serializers.ModelSerializer):
    hospital = RetrieveHospitalSerializer

    class Meta:
        model = Department
        fields = "__all__"
