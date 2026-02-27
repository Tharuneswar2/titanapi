class ModelPool:
    def __init__(self):
        self._models = {}

    def register(self, name: str, model):
        self._models[name] = model

    async def predict(self, name: str, input_data):
        if name not in self._models:
            raise ValueError("Model not found")
        model = self._models[name]
        return model(input_data)