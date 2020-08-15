from src.foundation.data.globalVar import GlobalVar
from src.foundation.event.listener import EventListener


class RunManager:
	on_stop = EventListener()

	@staticmethod
	def is_running():
		return GlobalVar.run

	@classmethod
	def stop(cls):
		GlobalVar.run = False
		cls.on_stop.trigger()
