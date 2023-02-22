from abc import ABC, abstractmethod

import battle.Stats


class AbstractEnemy(ABC):

    @abstractmethod
    def get_stat(self) -> battle.Stats.Stat:
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
