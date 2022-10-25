from celery import Celery
from celery_service.settings import Setting
from celery.schedules import crontab
app = Celery("celery service", broker=Setting.CELERY_BROKER, include=['tasks'])

app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'tasks.task.check',
        'schedule': crontab(minute="*/1")
    },

}

app.conf.timezone = Setting.CELERY_TIMEZONE
