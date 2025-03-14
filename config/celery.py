import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.deployment")
app = Celery("config")

app.conf.enable_utc = False
app.conf.timezone = 'Asia/Tashkent'


app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.update(
    broker_connection_retry_on_startup=True
)
app.conf.beat_schedule = {
    "fetch_weather_data_every_10_min": {
        "task": "src.core.tasks.fetch_weather_data",
        "schedule": crontab(minute="*/1"),  # Har 10 daqiqada
    },
}
app.autodiscover_tasks()
