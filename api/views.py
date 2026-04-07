from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DataJob
from .tasks import run_pipeline
from .serializers import DataJobSerializer

class TriggerPipeline(APIView):
    def post(self, request):
        source = request.data.get("source")

        job = DataJob.objects.create(source=source)

        run_pipeline.delay(job.id)

        return Response({"job_id": job.id})


class JobStatus(APIView):
    def get(self, request, job_id):
        job = DataJob.objects.get(id=job_id)
        serializer = DataJobSerializer(job)
        return Response(serializer.data)