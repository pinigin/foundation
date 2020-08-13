from src.foundation.singleton.singleton import Singleton


class Repository(Singleton):
    registry = []

    @classmethod
    def get_containers(cls) -> list:
        return cls.registry

    def singleton_init(self):
        containers = self.get_containers()
        self.containers = create_containers(containers)

    def get(self, container):
        return self.containers[container]


def create_containers(containers_list):
    containers = {}
    for container in containers_list:
        containers[container] = container()
    return containers
