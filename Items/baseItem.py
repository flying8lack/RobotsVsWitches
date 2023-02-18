from abc import ABC, abstractmethod
from util.dataStorage import DataStore
import pygame


class BaseItem(DataStore, ABC):

    @abstractmethod
    def update_location(self, newlocation: int):
        pass

    @abstractmethod
    def use(self, *args):
        pass

    @abstractmethod
    def get_texture_location(self) -> str:
        pass

    def get_rect(self) -> pygame.rect.Rect:
        return pygame.Rect(34 * self.location + 94, 94, 32, 32)

    @abstractmethod
    def get_surface(self) -> pygame.SurfaceType:
        pass
