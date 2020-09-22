class CoreInitializationManager:
	"""
	Class for initializing mcc models
	"""
	registry = []

	@classmethod
	def initialize(cls):
		"""
		that method will be invoked on Core initialization and will call method initialize() in all classes that inherits CoreInitializer
		"""
		for initializer in cls.registry:
			initializer.initialize()
