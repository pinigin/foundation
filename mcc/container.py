from src.foundation.mcc.repository import Repository


class Container(object):
    """
    base Class of Container
    Containers store models of data
    """

    def __init_subclass__(cls, **kwargs):
        Repository.registry.append(cls)

    def __init__(self):
        self.models = {}
