import json

from django.test import TestCase
from django.test import Client

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