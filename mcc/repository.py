from src.foundation.singleton.singleton import Singleton


class Repository(Singleton):
    """
    Singleton class that store containers, in which stores models of data
    """

    registry = []

    @classmethod
    def get_containers(cls) -> list:
        """
        return list of container classes
        """

        return cls.registry

    def singleton_init(self):
        """
        called only one time, and generate all containers which was inherits from Container class
        """
        containers = self.get_containers()
        self.containers = create_containers(containers)

    def get(self, container):
        """
        :param container: link of class
        :return: returning a container by link of class
        """
        return self.containers[container]


def create_containers(containers_list):
    """
    factory that generate containers
    """
    containers = {}
    for container in containers_list:
        containers[container] = container()
    return containers
