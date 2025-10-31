from rest_framework import serializers

from hospital.models import Hospital


class CreateDepartmentSerializer(serializers.Serializer):
    class Meta:
        model = Hospital
