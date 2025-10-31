from rest_framework.generics import RetrieveAPIView

from hospital.serializers.department import RetrieveDepartmentSerializer


class RetrieveDepartmentView(RetrieveAPIView):
    serializer_class = RetrieveDepartmentSerializer
