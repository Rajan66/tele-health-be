from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from gatekeeper.views.zego import ZegoTokenAPIView

urlpatterns = [
    path(
        "",
        TokenObtainPairView.as_view(),
        name="get_token",
    ),
    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="refresh_token",
    ),
    path(
        "zego/",
        ZegoTokenAPIView.as_view(),
        name="zego_token",
    ),
]
