from django.contrib import admin

from worker.models import HealthWorker

admin.site.register(HealthWorker)
