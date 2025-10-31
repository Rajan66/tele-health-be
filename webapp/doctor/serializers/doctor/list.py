from rest_framework import serializers  # noqa
from doctor.models import Doctor
from hospital.serializers.department import ListDepartmentSerializer


class ListDoctorSerializer(serializers.ModelSerializer):
    department = ListDepartmentSerializer(read_only=True)

    class Meta:
        model = Doctor
        fields = "__all__"
