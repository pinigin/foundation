from src.foundation.mcc.container import Container


class ContainerController:
    def __init__(self, container: Container):
        self.container = container

    def add_model(self, name: str, model) -> bool:
        if name not in self.container.models:
            self.container.models[name] = model
            return True
        return False
