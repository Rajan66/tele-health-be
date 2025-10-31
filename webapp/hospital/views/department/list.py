from rest_framework.generics import ListAPIView

from hospital.serializers.department import ListDepartmentSerializer


class ListDepartmentView(ListAPIView):
    serializer_class = ListDepartmentSerializer
