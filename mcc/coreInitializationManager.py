class CoreInitializationManager:
	registry = []

	@classmethod
	def initialize(cls):
		for initializer in cls.registry:
			initializer.initialize()