from rest_framework import serializers

from hospital.models import Department


class UpdateDepartmentSerializer(serializers.Serializer):
    name = serializers.CharField()

    class Meta:
        model = Department
