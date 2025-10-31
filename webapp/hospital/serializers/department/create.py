from rest_framework import serializers  # noqa
from hospital.models import Department


class CreateDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
