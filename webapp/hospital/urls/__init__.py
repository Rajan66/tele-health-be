from django.urls import include, path  # noqa

from hospital.urls import hospital, department

urlpatterns = [
    path("hospital/", include(hospital.urlpatterns)),
    path("department/", include(department.urlpatterns)),
]
