from typing import List

import pygame

import Items.baseItem
import util.constants


class Inventory:
    INV_MAX_LENGTH = 4

    def __init__(self):
        self.inventory: List[Items.baseItem.BaseItem] = []
        self._open = False
        self.surface = pygame.Surface((util.constants.SCREEN_WIDTH, util.constants.SCREEN_HEIGHT))

    def draw_surface(self) -> bool:
        if not self._open:
            return False
        else:
            pygame.draw.rect(self.surface)
            return True

    def set_open(self, state: bool):
        self._open = state

    def close_inventory(self):
        self.set_open(False)

    def is_full(self):
        return len(self.inventory) == self.INV_MAX_LENGTH

    def insert_item(self, index: int, item: Items.baseItem.BaseItem) -> bool:
        if not self.is_full():
            self.inventory.insert(index, item)
            return True
        return False

    def remove_item(self, index: int) -> bool:
        if len(self.inventory) >= index:
            self.inventory.pop(index)
            return True
        return False
