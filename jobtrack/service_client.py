import requests

from django.urls import reverse


# stub
def submit_job(job_body, job_callback):
    # print(
    #     f"stub: would submit job with body = {job_body!r} and callback {job_callback!r}"
    # )
    pass


# real client
def submit_job_real(job_body, job_callback):
    r = requests.post(
        "http://example.com/requests",
        json={
            body: job_body,
            callback: job_callback,
        },
    )
    r.raise_for_status()
