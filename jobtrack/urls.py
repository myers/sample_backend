from django.urls import path

from . import views

urlpatterns = [
    path("request", views.add_job, name="add-job"),
    path("callback/<uuid:job_uuid>", views.job_callback, name="job-callback"),
]
