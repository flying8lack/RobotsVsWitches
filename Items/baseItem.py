from abc import ABC, abstractmethod


class BaseItem(ABC):

    @abstractmethod
    def get_texture_location(self):
        pass

    @abstractmethod
    def get_rect(self):
        pass

    @abstractmethod
    def get_surface(self):
        pass
