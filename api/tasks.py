from celery import shared_task
from .models import DataJob
from .utils import transform
from .adapters import fetch_from_source

@shared_task
def run_pipeline(job_id):
    job = DataJob.objects.get(id=job_id)

    job.status = 'running'
    job.save()

    data = fetch_from_source(job.source)
    processed = transform(data)

    job.result = processed
    job.status = 'completed'
    job.save()