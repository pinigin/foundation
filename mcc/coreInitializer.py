from src.foundation.mcc.coreInitializationManager import CoreInitializationManager


class CoreInitializer:
	"""
	Parent class of all initialization classes, that will be called on init of core
	"""
	@classmethod
	def initialize(cls):
		"""
		method that will be called on core initialization
		"""
		raise NotImplementedError

	def __init_subclass__(cls, **kwargs):
		CoreInitializationManager.registry.append(cls)
