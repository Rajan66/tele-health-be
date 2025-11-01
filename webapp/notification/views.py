from django.db import models
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from notification.models import Notification
from notification.serializers import (
    NotificationSerializer,
    UpdateNotificationSerializer,
)


class NotificationListAPIView(ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(
            models.Q(doctor=user) | models.Q(health_worker=user)
        ).order_by("-created_at")


class NotificationMarkAsReadAPIView(UpdateAPIView):
    serializer_class = UpdateNotificationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(
            models.Q(doctor=user) | models.Q(health_worker=user)
        )

    def patch(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        serializer = self.get_serializer(notification)
        return Response(serializer.data)


class NotificationMarkAllAsReadAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = None

    def post(self, request):
        user = request.user
        notifications = Notification.objects.filter(
            models.Q(doctor=user) | models.Q(health_worker=user), is_read=False
        )
        count = notifications.count()
        notifications.update(is_read=True)
        return Response({"detail": f"{count} notifications marked as read"})
