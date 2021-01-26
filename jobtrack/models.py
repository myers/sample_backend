import uuid

from django.db import models

STATUS_CHOICES = [
    ("STARTED", "Started"),
    ("PROCESSED", "Processed"),
    ("COMPLETED", "Completed"),
    ("ERROR", "Error"),
]


class Job(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    body = models.TextField()
    detail = models.TextField()
