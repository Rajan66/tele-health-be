from django.urls import include, path

from gatekeeper.urls import token, user

urlpatterns = [
    path("token/", include(token.urlpatterns)),
    path("user/", include(user.urlpatterns)),
]
