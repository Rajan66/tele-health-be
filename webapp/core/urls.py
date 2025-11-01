from django.contrib import admin  # noqa

from django.conf import settings as S
from django.conf.urls.static import static

from django.urls import include, path
from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.authentication import BasicAuthentication

# swagger config
from rest_framework.permissions import IsAdminUser

urlpatterns = []

BASIC_AUTH_PROTECTION = {
    "authentication_classes": [BasicAuthentication],
    "permission_classes": [IsAdminUser],
}

urlpatterns += [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "swagger/schema/",
        SpectacularJSONAPIView.as_view(**BASIC_AUTH_PROTECTION),
        name="api_schema",
    ),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(
            url_name="api_schema",
            **BASIC_AUTH_PROTECTION,
        ),
        name="api_swagger",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(
            url_name="api_schema",
            **BASIC_AUTH_PROTECTION,
        ),
        name="api_redoc",
    ),
]


urlpatterns += [
    path("gatekeeper/", include("gatekeeper.urls")),
    path("hospital/", include("hospital.urls")),
    path("doctor/", include("doctor.urls")),
    # path("worker/", include("worker.urls")),
    path("appointment/", include("appointment.urls")),
    path("notification/", include("notification.urls")),
    path("patient/", include("patient.urls")),
    path("report/", include("report.urls")),
] + static(S.MEDIA_URL, document_root=S.MEDIA_ROOT)
