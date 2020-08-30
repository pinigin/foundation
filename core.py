import time

from src.foundation.mcc.coreInitializationManager import CoreInitializationManager
from src.foundation.runManager import RunManager
from src.foundation.singleton.serviceManager import ServiceManager
from src.foundation.singleton.singleton import Singleton
from src.foundation.tasks.taskManager import TaskManager
from src.foundation.util import file, thread
from src.foundation.util.logger import get_logger

logger = get_logger(__name__)


class Core(Singleton):
	def singleton_init(self):
		logger.info("starting init of core")
		file.init_folders()
		self.task_manager = TaskManager()
		CoreInitializationManager.initialize()
		ServiceManager()
		logger.info("finished init of core")

	def start(self):
		thread.run_in_new_thread(True, "task_loop", self.task_loop)
		thread.run_in_new_thread(False, "main_loop", self.loop)

	def loop(self):
		while RunManager.is_running():
			time.sleep(0.01)

	def task_loop(self):
		while RunManager.is_running():
			self.task_manager.run()
			time.sleep(0.01)
