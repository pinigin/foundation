from src.foundation.mcc.repository import Repository


class Container(object):
    def __init_subclass__(cls, **kwargs):
        Repository.registry.append(cls)

    def __init__(self):
        self.models = {}
