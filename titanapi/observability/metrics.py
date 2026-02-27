def setup_metrics(app):
    try:
        from prometheus_fastapi_instrumentator import Instrumentator
    except ImportError:
        raise RuntimeError(
            "Observability requires 'prometheus-fastapi-instrumentator'. "
            "Install it with: pip install prometheus-fastapi-instrumentator"
        )

    Instrumentator().instrument(app).expose(app)