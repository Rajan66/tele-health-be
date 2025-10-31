from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from notification.models import Notification
from .serializers import NotificationSerializer


class NotificationListAPIView(ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by(
            "-created_at"
        )


class NotificationMarkAsReadAPIView(UpdateAPIView):
    serializer_class = NotificationSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        serializer = self.get_serializer(notification)
        return Response(serializer.data)


class NotificationMarkAllAsReadAPIView(APIView):
    def post(self, request):
        notifications = Notification.objects.filter(
            user=request.user, is_read=False
        )
        count = notifications.count()
        notifications.update(is_read=True)
        return Response({"detail": f"{count} notifications marked as read"})
