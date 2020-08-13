from src.foundation.singleton.services import ServiceManager


class Service:
	def __init_subclass__(cls, **kwargs):
		ServiceManager.registry.append(cls)
