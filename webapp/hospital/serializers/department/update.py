from rest_framework import serializers

from hospital.models import Department


class UpdateDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department

        fields = "__all__"

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
