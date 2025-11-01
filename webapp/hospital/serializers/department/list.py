from rest_framework import serializers

from hospital.models import Department


class ListDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
