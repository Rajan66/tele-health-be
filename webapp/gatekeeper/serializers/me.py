from rest_framework import serializers

from gatekeeper.models import User


class RetrieveMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "role",
        ]
