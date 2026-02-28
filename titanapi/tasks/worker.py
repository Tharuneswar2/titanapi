from arq import cron
from arq.worker import Worker
from arq.connections import RedisSettings
from titanapi import titan

async def heartbeat(ctx):
    print("💓 Titan Worker Heartbeat Running")


class TitanWorker(Worker):
    def __init__(self):
        super().__init__(
            redis_settings=RedisSettings(),
            cron_jobs=[
                cron(heartbeat),
            ],
            functions=list(titan.task_registry.all().values()),

        )
        
