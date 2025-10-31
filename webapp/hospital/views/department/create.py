from rest_framework.generics import CreateAPIView

from hospital.serializers.department import CreateDepartmentSerializer


class CreateDepartmentView(CreateAPIView):
    serializer_class = CreateDepartmentSerializer
