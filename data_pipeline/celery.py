import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_pipeline.settings')

app = Celery('data_pipeline')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()