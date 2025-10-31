from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from gatekeeper.serializers import RetrieveMeSerializer


class RetrieveMeView(RetrieveAPIView):
    serializer_class = RetrieveMeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
