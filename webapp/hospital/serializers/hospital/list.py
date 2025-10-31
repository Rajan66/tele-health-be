from rest_framework import serializers

from hospital.models import Hospital


class ListHospitalSerializer(serializers.Serializer):
    class Meta:
        model = Hospital
        fields = "__all__"
