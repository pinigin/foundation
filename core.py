import time

from src.foundation.mcc.coreInitializationManager import CoreInitializationManager
from src.foundation.singleton.serviceManager import ServiceManager
from src.foundation.singleton.singleton import Singleton
from src.foundation.tasks.taskManager import TaskManager
from src.foundation.util import file, thread


class Core(Singleton):
	def singleton_init(self):
		file.init_folders()
		self.task_manager = TaskManager()
		CoreInitializationManager.initialize()
		ServiceManager()

	def start(self):
		thread.run_in_new_thread(True, "task_loop", self.task_loop)
		thread.run_in_new_thread(False, "main_loop", self.loop)

	def loop(self):
		while True:
			time.sleep(0.01)

	def task_loop(self):
		while True:
			self.task_manager.run()
			time.sleep(0.01)
