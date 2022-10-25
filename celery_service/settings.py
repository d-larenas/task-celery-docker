from environs import Env

env = Env()

CELERY_BROKER = env("CELERY_BROKER", "redis://localhost:6379/0")

CELERY_TIMEZONE = env("CELERY_TIMEZONE", "UTC")

