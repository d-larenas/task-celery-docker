ARG PYTHON_VERSION=3.9-slim-buster
FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=base

WORKDIR /app
# Requirements are installed here to ensure they will be cached.
COPY ./requirements/ .
# Create Python Dependency and Sub-Dependency Wheels.
RUN pip install -r ${BUILD_ENVIRONMENT}.txt

COPY ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY celery_service app
COPY tasks app

RUN echo $PYTHONPATH


