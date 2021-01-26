import json

from django.test import TestCase
from django.test import Client

class JobTrackAPITests(TestCase):
    def test_submit_job(self):
        body = {"body": "cheese gromit!"}
        response = self.client.post(
            "/request", json.dumps(body), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
