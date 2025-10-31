from django.urls import path

from hospital.views.department import (
    CreateDepartmentView,
    ListDepartmentView,
    RetrieveDepartmentView,
    UpdateDepartmentView,
)

urlpatterns = [
    path(
        "create/",
        CreateDepartmentView.as_view(),
        name="create-department",
    ),
    path(
        "list/",
        ListDepartmentView.as_view(),
        name="list-department",
    ),
    path(
        "retrieve/<uuid:pk>",
        RetrieveDepartmentView.as_view(),
        name="create-department",
    ),
    path(
        "update/<uuid:pk>",
        UpdateDepartmentView.as_view(),
        name="update-department",
    ),
]
