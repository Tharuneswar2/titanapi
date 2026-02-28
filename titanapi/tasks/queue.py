from arq import create_pool
from arq.connections import RedisSettings
from arq import create_pool
from arq.connections import RedisSettings

redis_settings = RedisSettings()

async def enqueue_task(task_name: str, *args, **kwargs):
    pool = await create_pool(redis_settings)
    await pool.enqueue_job(task_name, *args, **kwargs)
class TaskQueue:
    def __init__(self, redis_url="redis://localhost:6379/0"):
        self.redis_settings = RedisSettings.from_dsn(redis_url)
        self._redis = None

    async def connect(self):
        if not self._redis:
            self._redis = await create_pool(self.redis_settings)

    async def enqueue(self, task_name: str, *args):
        await self.connect()
        return await self._redis.enqueue_job(task_name, *args) # type: ignore