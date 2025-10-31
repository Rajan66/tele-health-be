from rest_framework import serializers  # noqa
from doctor.models import Doctor


class ListDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
