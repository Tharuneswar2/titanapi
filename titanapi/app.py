from fastapi import FastAPI

class TitanAPI:
    def __init__(
        self,
        *,
        title: str = "TitanAPI App",
        distributed: bool = False,
        ai: bool = False,
        observability: bool = True,
    ):
        self._app = FastAPI(title=title)
        self.config = {
            "distributed": distributed,
            "ai": ai,
            "observability": observability,
        }

        if observability:
            self._setup_observability()

        if distributed:
            self._setup_tasks()

        if ai:
            self._setup_ai()

    # -------------------
    # Route Forwarding
    # -------------------
    def get(self, *args, **kwargs):
        return self._app.get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self._app.post(*args, **kwargs)

    def include_router(self, router):
        return self._app.include_router(router)

    @property
    def fastapi(self):
        return self._app

    # -------------------
    # Internal Modules
    # -------------------
    def _setup_tasks(self):
        from titanapi.tasks.queue import TaskQueue
        self.tasks = TaskQueue()
        self._app.state.tasks = self.tasks

    def _setup_ai(self):
        from titanapi.ai.model_pool import ModelPool
        self.ai = ModelPool()
        self._app.state.ai = self.ai

    def _setup_observability(self):
        from titanapi.observability.metrics import setup_metrics
        setup_metrics(self._app)