from src.foundation.data.globalVar import GlobalVar
from src.foundation.event.listener import EventListener


class RunManager:
	# event that will be trigger on applications stops
	on_stop = EventListener()

	@staticmethod
	def is_running():
		"""return if application is running"""
		return GlobalVar.run

	@classmethod
	def stop(cls):
		"""stop application"""
		GlobalVar.run = False
		cls.on_stop.trigger()
