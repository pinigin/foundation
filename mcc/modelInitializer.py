from src.foundation.mcc.modelInitializationManager import ModelInitializationManager


class ModelInitializer:
	def initialize(self):
		raise NotImplementedError

	def __init_subclass__(cls, **kwargs):
		ModelInitializationManager.registry.append(cls)
