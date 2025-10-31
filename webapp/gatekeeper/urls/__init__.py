from django.urls import include, path

from gatekeeper.urls import token

urlpatterns = [
    path("token/", include(token.urlpatterns)),
]
