from django.urls import include, path  # noqa

from hospital.urls import hospital, department

urlpatterns = [
    path("", include(hospital.urlpatterns)),
    path("department/", include(department.urlpatterns)),
]
