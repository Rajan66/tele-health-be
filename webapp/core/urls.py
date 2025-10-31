"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
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
]
