from src.foundation.singleton.serviceManager import ServiceManager


class Service:
	"""
	Parent class of all services.
	Service is a class that handle a connection, and is created in start of application.
	service can not have constructor with params
	"""
	def __init_subclass__(cls, **kwargs):
		ServiceManager.registry.append(cls)
