import json

from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .models import Job


class JobTrackAPITests(TestCase):
    def test_submit_job(self):
        self.assertEqual(0, Job.objects.count())
        body = {"body": "cheese gromit!"}
        response = self.client.post(
            "/request", json.dumps(body), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, Job.objects.count())

    def test_job_callback_started(self):
        job = Job.objects.create(body=json.dumps({"body": "cheese gromit!"}))
        response = self.client.post(
            job.callback_url(), "STARTED", content_type="text/plain"
        )
        self.assertEqual(response.status_code, 204)
        job.refresh_from_db()
        self.assertEqual("STARTED", job.status)
