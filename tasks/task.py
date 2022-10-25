from celery_service import celery_app as app


@app.task
def check():
    print("I am checking your stuff")

