from django.contrib import admin  # noqa

from hospital.models import Hospital, Department

admin.site.register(Hospital)
admin.site.register(Department)
