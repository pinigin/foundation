class ModelInitializationManager:
	registry = []

	@classmethod
	def initialize(cls):
		for initializer in cls.registry:
			initializer.initialize()