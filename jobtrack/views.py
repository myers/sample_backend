import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Job

from .service_client import submit_job


@csrf_exempt
def add_job(request):
    if request.content_type != "application/json":
        return HttpResponseBadRequest("content must be of type application/json")
    # should test body is vaild utf-8
    # should test body content is valid JSON
    doc = json.loads(request.body.decode("utf-8"))
    job = Job.objects.create(body=doc["body"])

    job_callback = request.build_absolute_uri(job.callback_url())
    # if we encounter an error posting this to the service this request will raise an exception and because we have ATOMIC_REQUESTS set in the settings the transaction we are in will rollback.  It would be a good idea for us to pass on error messages from the service to our clients, using 502 http status codes.  Also might consider using a service like Sentry or BugSnag and report an error via that service for better ops visibilty into errors from the service.
    submit_job(job.body, job_callback)
    return HttpResponse(job.uuid)


@csrf_exempt
def job_callback(request, job_uuid):
    if request.method == "POST":
        return job_callback_post(request, job_uuid)
    elif request.method == "PUT":
        return job_callback_put(request, job_uuid)
    else:
        return HttpResponseBadRequest("Only accept POST and PUT")


def job_callback_post(request, job_uuid):
    request_body = request.body.decode("utf-8")
    assert request_body == "STARTED", f"{request_body!r}"
    job = get_object_or_404(Job, uuid=job_uuid)
    job.status = request_body
    job.save()
    return HttpResponse(status=204)


def job_callback_put(request, job_uuid):
    job = get_object_or_404(Job, uuid=job_uuid)
    body = json.loads(request.body.decode("utf-8"))
    assert body.get("status") in ["PROCESSED", "COMPLETED", "ERROR"]
    job.status = body.get("status")
    job.detail = body.get("detail")
    job.save()

    return HttpResponse(status=204)


def job_status(request, job_uuid):
    job = get_object_or_404(Job, uuid=job_uuid)
    return JsonResponse({"status": job.status, "body": job.body, "detail": job.detail})
