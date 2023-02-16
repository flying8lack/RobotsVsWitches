from abc import ABC, abstractmethod

import pygame


class BaseItem(ABC):

    @abstractmethod
    def get_texture_location(self) -> str:
        pass

    @abstractmethod
    def get_rect(self):
        pass

    @abstractmethod
    def get_surface(self) -> pygame.SurfaceType:
        pass
