from src.foundation.singleton.singleton import Singleton


class ServiceManager(Singleton):
    """
    Singleton class that store services, which can be get by link of service class
    """

    registry = []

    def singleton_init(self):
        services = self.get_services()
        self.services = create_services(services)

    @classmethod
    def get_services(cls) -> list:
        return cls.registry

    def get_service(self, service):
        if service in self.services:
            self.services[service] = service()
        return self.services[service]


def create_services(services_list: list) -> dict:
    services = {}
    for service in services_list:
        services[service] = service()
    return services
