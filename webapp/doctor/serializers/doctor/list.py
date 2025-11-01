from rest_framework import serializers

from doctor.models import Doctor
from hospital.serializers.department import ListDepartmentSerializer
from gatekeeper.serializers import RetrieveMeSerializer


class ListDoctorSerializer(serializers.ModelSerializer):
    department = ListDepartmentSerializer(read_only=True)
    user = RetrieveMeSerializer(read_only=True)
    hospital = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = "__all__"

    def get_hospital(self, obj):
        if obj.department and obj.department.hospital:
            from hospital.serializers.hospital.list import (
                ListHospitalSerializer,
            )

            return ListHospitalSerializer(obj.department.hospital).data
        return None
