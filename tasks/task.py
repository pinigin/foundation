class Task:
    """
        Base Task class for async operations
    """

    def __init__(self, task):
        self.__task_name = task
        self.closed = False
        self.started = False
        self.id = 0

    def run(self):
        """
            Callable every second
        """

    def start(self):
        """
            Callable when task started
        """

        self.started = True
