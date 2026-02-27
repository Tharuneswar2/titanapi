class TaskQueue:
    def __init__(self):
        self._tasks = {}

    def task(self, fn):
        self._tasks[fn.__name__] = fn
        return fn

    async def enqueue(self, name: str, *args, **kwargs):
        if name not in self._tasks:
            raise ValueError(f"Task {name} not found")

        # Temporary: run inline (Phase 1)
        return await self._tasks[name](*args, **kwargs)