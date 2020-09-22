from src.foundation.mcc.container import Container


class ContainerController:
    """
    base Class of Container Controller.
    Containers Controllers need to edit containers
    """

    def __init__(self, container: Container):
        self.container = container

    def add_model(self, name: str, model) -> bool:
        """
        Add model to Container
        """
        if name not in self.container.models:
            self.container.models[name] = model
            return True
        return False
