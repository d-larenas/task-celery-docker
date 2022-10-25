from .celery_app import app as celery_app
from .settings import Setting

__all__ = ('celery_app',)