from celery import shared_task


@shared_task
def hello_world_task():
    print("Hello celery ;)")
