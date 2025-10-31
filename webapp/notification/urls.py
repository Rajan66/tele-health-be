# notification/urls.py
from django.urls import path
from .views import (
    NotificationListAPIView,
    NotificationMarkAsReadAPIView,
    NotificationMarkAllAsReadAPIView,
)

urlpatterns = [
    path(
        "notifications/list",
        NotificationListAPIView.as_view(),
        name="notification-list",
    ),
    path(
        "notifications/<uuid:id>/mark-as-read/",
        NotificationMarkAsReadAPIView.as_view(),
        name="notification-mark-as-read",
    ),
    path(
        "notifications/mark-all-as-read/",
        NotificationMarkAllAsReadAPIView.as_view(),
        name="notification-mark-all-as-read",
    ),
]
