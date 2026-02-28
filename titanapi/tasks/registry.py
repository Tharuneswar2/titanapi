class TaskRegistry:
    def __init__(self):
        self._tasks = {}

    def register(self, name: str, func):
        self._tasks[name] = func

    def get(self, name: str):
        return self._tasks.get(name)

    def all(self):
        return self._tasks