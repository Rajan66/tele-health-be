from django.urls import path

from hospital.views.department import (
    CreateDepartmentView,
    ListDepartmentView,
    RetrieveDepartmentView,
    UpdateDepartmentView,
)

urlpatterns = [
    path(
        "",
        CreateDepartmentView.as_view(),
        name="create-department",
    ),
    path(
        "",
        ListDepartmentView.as_view(),
        name="list-department",
    ),
    path(
        "",
        RetrieveDepartmentView.as_view(),
        name="create-department",
    ),
    path(
        "",
        UpdateDepartmentView.as_view(),
        name="update-department",
    ),
]
