from celery import Celery
from .settings import CELERY_BROKER, CELERY_TIMEZONE
from celery.schedules import crontab
app = Celery("celery service", broker=CELERY_BROKER, include=['tasks'])

app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'tasks.task.check',
        'schedule': crontab(minute="*/1")
    },

}

app.conf.timezone = CELERY_TIMEZONE
