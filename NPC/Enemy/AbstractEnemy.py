from abc import ABC, abstractmethod


class AbstractEnemy(ABC):
    @abstractmethod
    def get_stat(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_surface(self):
        pass

    @abstractmethod
    def get_battle_surface(self):
        pass

    @abstractmethod
    def get_battle_rect(self):
        pass

    @abstractmethod
    def get_rect(self):
        pass
