from src.foundation.singleton.singleton import Singleton


class HandlerRepository(Singleton):
	def singleton_init(self):
		self.handlers = {}
