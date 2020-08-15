from src.foundation.util.logger import get_logger

logger = get_logger(__name__)


class EventListener:
    def __init__(self):
        self._actions = []

    def subscribe(self, action):
        """
        subscribe action on this EventListener
        :param action: action to subscribe
        """
        if callable(action):
            self._actions.append(action)
        else:
            logger.error("try to subscribe action that is not callable")

    def trigger(self, *args, **kwargs):
        """
        trigger actions of this EventListener
        """
        for action in self._actions:
            try:
                action(*args, **kwargs)
            except Exception as e:
                logger.exception(e)

    def unsubscribe(self, action) -> bool:
        """
        unsubscribe action from this EventListener
        :param action: action to unsubscribe
        """
        if action in self._actions:
            self._actions.remove(action)
            return True
        return False
