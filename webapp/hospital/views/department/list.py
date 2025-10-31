from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from hospital.serializers.department import ListDepartmentSerializer
from hospital.models import Department


class ListDepartmentView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = ListDepartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "name": ["icontains"],
    }
