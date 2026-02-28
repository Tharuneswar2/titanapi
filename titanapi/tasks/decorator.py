from functools import wraps
from titanapi.tasks.registry import TaskRegistry
from titanapi.tasks.queue import enqueue_task

class TitanTask:

    def __init__(self, registry: TaskRegistry):
        self.registry = registry

    def __call__(self, func):
        task_name = func.__name__
        self.registry.register(task_name, func)

        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        async def delay(*args, **kwargs):
            await enqueue_task(task_name, *args, **kwargs)

        wrapper.delay = delay
        return wrapper