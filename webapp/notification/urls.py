# notification/urls.py
from django.urls import path
from .views import (
    NotificationListAPIView,
    NotificationMarkAsReadAPIView,
    NotificationMarkAllAsReadAPIView,
)

urlpatterns = [
    path(
        "list/",
        NotificationListAPIView.as_view(),
        name="notification-list",
    ),
    path(
        "<uuid:id>/mark-as-read/",
        NotificationMarkAsReadAPIView.as_view(),
        name="notification-mark-as-read",
    ),
    path(
        "mark-all-as-read/",
        NotificationMarkAllAsReadAPIView.as_view(),
        name="notification-mark-all-as-read",
    ),
]
