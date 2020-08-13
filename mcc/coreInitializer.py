from src.foundation.mcc.coreInitializationManager import CoreInitializationManager


class CoreInitializer:
	@classmethod
	def initialize(cls):
		raise NotImplementedError

	def __init_subclass__(cls, **kwargs):
		CoreInitializationManager.registry.append(cls)
