import os
import ssl

from celery import Celery

# We use amqp for RabbitMQ broker by default
RABBITMQ_URL = os.environ.get("CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672//")

celery_app = Celery(
    "migration_worker",
    broker=RABBITMQ_URL,
    include=["mule_parser.api.execution"]
)

celery_conf = {
    "task_serializer": "json",
    "accept_content": ["json"],
    "result_serializer": "json",
    "timezone": "UTC",
    "enable_utc": True,
    "task_ignore_result": True,
}

if RABBITMQ_URL.startswith("amqps://"):
    celery_conf.update(
        broker_use_ssl={"ssl_cert_reqs": ssl.CERT_NONE},
    )

celery_app.conf.update(**celery_conf)
