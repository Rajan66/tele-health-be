from rest_framework import serializers
from .models import Report


class CreateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
        read_only_fields = ["created_by", "report_date"]


class ListReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"


class RetrieveReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"


class UpdateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
