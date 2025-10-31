from rest_framework import serializers  # noqa
from hospital.models import Hospital


class ListHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"
