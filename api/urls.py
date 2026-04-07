from django.urls import path
from .views import TriggerPipeline, JobStatus

urlpatterns = [
    path('trigger/', TriggerPipeline.as_view()),
    path('status/<int:job_id>/', JobStatus.as_view()),
]