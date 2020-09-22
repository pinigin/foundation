from src.foundation.mcc.model import Model


class ModelController:
	"""
	Parent class of all models controllers.
	models controllers is needed to change data in models.
	"""
	def __init__(self, model: Model):
		"""
		:param model: model with which the controller can work.
		"""
		self.model = model
