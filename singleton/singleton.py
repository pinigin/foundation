class Singleton:
	"""
	singleton is a class that has global access and exists in a single instance
	"""
	_instance = None
	was_initialized = False

	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not self.was_initialized:
			self.was_initialized = True
			self.singleton_init()

	def singleton_init(self):
		pass

