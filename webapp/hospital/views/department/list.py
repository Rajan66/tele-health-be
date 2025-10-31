from rest_framework.generics import ListAPIView  # noqa

from hospital.serializers.department import ListDepartmentSerializer
from hospital.models import Department


class ListDepartmentView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = ListDepartmentSerializer
