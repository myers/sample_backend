import uuid

from django.db import models
from django.urls import reverse

STATUS_CHOICES = [
    ("STARTED", "Started"),
    ("PROCESSED", "Processed"),
    ("COMPLETED", "Completed"),
    ("ERROR", "Error"),
]


class Job(models.Model):
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append((field.name, str(getattr(self, field.name, ""))))
        return str(field_values)

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    body = models.TextField()
    detail = models.TextField()

    def callback_url(self):
        return reverse("job-callback", kwargs=dict(job_uuid=self.uuid))
