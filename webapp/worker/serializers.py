from rest_framework import serializers
from worker.models import HealthWorker


class RetrieveWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthWorker
        fields = "__all__"
