from rest_framework.generics import RetrieveAPIView

from gatekeeper.serializers import RetrieveMeSerializer


class RetrieveMeView(RetrieveAPIView):
    serializer_class = RetrieveMeSerializer

    def get_object(self):
        return self.request.user
