# Python + Celery + Docker

Application for scheduled tasks with celery.

## Installation

Add env.example variable file.

```
  .envs -> path
  └── .local ->file
     
```

## docker 

```
    docker-compose -f local.yml build

    docker-compose -f local.yml up

```

## celery extra

```
    celery -A celery_service worker -l INFO

    celery -A celery_service beat -l INFO

```