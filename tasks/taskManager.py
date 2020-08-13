from src.foundation.util.logger import get_logger
from src.foundation.tasks.task import Task

logger = get_logger(__name__)


class TaskManager:
	def __init__(self):
		self.task_list = {}
		self._task_id_inc = -1

	def add_task(self, task: Task):
		"""
			Add task to task manager
		"""

		self._task_id_inc += 1
		task.id = self._task_id_inc
		self.task_list[self._task_id_inc] = task
		return self._task_id_inc

	def run(self):
		"""
			Run all tasks
		"""

		keys = list(self.task_list.keys())
		for task_id in keys:
			task = self.task_list[task_id]
			try:
				if not task.started:
					task.start()
				else:
					if task.closed:
						task = self.task_list.pop(task_id)
						logger.debug(f"close task {task} with id {task.id}")
					else:
						task.run()
			except Exception as e:
				logger.exception(e)
				task.closed = True

	def run_callback(self, task_id: int, data: dict):
		"""
			Run task callback on data arrived from client
		"""

		if task_id in self.task_list:
			self.task_list[task_id].callback(data)
