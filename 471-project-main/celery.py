import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT_471.settings')
app = Celery('PROJECT_471')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()