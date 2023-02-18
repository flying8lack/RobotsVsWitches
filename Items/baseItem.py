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

    @abstractmethod
    def get_rect(self) -> pygame.rect.Rect:
        pass

    @abstractmethod
    def get_surface(self) -> pygame.SurfaceType:
        pass
