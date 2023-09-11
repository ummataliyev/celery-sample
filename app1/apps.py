from django.apps import AppConfig
from django.core.exceptions import ValidationError


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'

    def ready(self) -> None:
        from django_celery_beat.models import PeriodicTask, IntervalSchedule
        try:
            schedule, created = IntervalSchedule.objects.get_or_create(
                every=10,
                period=IntervalSchedule.SECONDS,
            )
            PeriodicTask.objects.create(
                interval=schedule,                   # we created this above.
                name='hello world task',             # simply describes this periodic task.
                task='app1.tasks.hello_world_task',  # name of task.
            )
        except ValidationError:
            pass

        return super().ready()
