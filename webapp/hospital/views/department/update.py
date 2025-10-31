from rest_framework.generics import UpdateAPIView

from hospital.serializers.department import UpdateDepartmentSerializer


class UpdateDepartmentView(UpdateAPIView):
    serializer_class = UpdateDepartmentSerializer
