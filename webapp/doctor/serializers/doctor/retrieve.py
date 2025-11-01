from rest_framework import serializers

from doctor.models import Doctor
from gatekeeper.serializers import RetrieveMeSerializer
from hospital.serializers.department import RetrieveDepartmentSerializer


class RetrieveDoctorSerializer(serializers.ModelSerializer):
    user = RetrieveMeSerializer()

    department = RetrieveDepartmentSerializer()

    class Meta:
        model = Doctor
        fields = "__all__"


class RetrieveNanoDoctorSerializer(serializers.ModelSerializer):
    user = RetrieveMeSerializer()

    class Meta:
        model = Doctor
        fields = (
            "id",
            "user",
            "created_at",
            "updated_at",
        )
