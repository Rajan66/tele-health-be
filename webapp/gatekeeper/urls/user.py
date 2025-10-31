from django.urls import path

from gatekeeper.views.me import RetrieveMeView

urlpatterns = [
    path(
        "me/",
        RetrieveMeView.as_view(),
        name="retrieve-me",
    ),
]
