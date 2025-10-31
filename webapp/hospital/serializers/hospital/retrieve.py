from rest_framework import serializers

from hospital.models import Hospital


class RetrieveHospitalSerializer(serializers.Serializer):
    class Meta:
        model = Hospital
        fields = "__all__"
