import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_p.settings')

app = Celery('celery_p')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'every-5-seconds': {
    #     'task': "<app_name>.tasks.hello", # path of the task
    #     "schedule": 1,
    # },
    'every-5-seconds': {
        'task': "projectApp.tasks.add",
        "schedule": 150,
        'args': (16, 16)
    }
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
