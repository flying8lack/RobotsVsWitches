import logging
from typing import List, Optional

import pygame

import Items.baseItem
import util.constants
from util.dataStorage import DataStore


class Inventory(DataStore):
    def saveData(self):
        pass

    def readData(self):
        pass

    INV_MAX_LENGTH = 4

    def __init__(self):
        self.inventory: List[Items.baseItem.BaseItem] = []
        self._open: bool = False
        self.surface = pygame.Surface((util.constants.SCREEN_WIDTH, util.constants.SCREEN_HEIGHT))
        self._main_hand: Optional[Items.baseItem.BaseItem] = None
        self._select_item: Optional[Items.baseItem.BaseItem] = None

    @property
    def select_item(self):
        return self._select_item

    @select_item.setter
    def select_item(self, value: Optional[Items.baseItem.BaseItem]):
        self._select_item = value

    @select_item.deleter
    def select_item(self):
        self._select_item = None

    @property
    def main_hand(self):
        return self._main_hand

    @main_hand.setter
    def main_hand(self, item):
        self._main_hand = item

    @main_hand.deleter
    def main_hand(self):
        self._main_hand = None

    def toggle_open(self):
        self.set_open(not self._open)

    def is_open(self) -> bool:
        return self._open

    def process_inventory_event(self, event: pygame.event.Event):
        logging.debug("processing inventory event")
        if not self._open:
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(4):
                if self.inventory[i] is None:
                    continue
                else:
                    if self.inventory[i].get_rect().collidepoint(event.pos[0], event.pos[1]):
                        self.select_item = self.inventory[i]
                        logging.info(f"selected item from slot {i}")

    def draw_item(self, index: int):

        if self.inventory[index] is None:
            return

        self.surface.blit(self.inventory[index].get_surface(),
                          self.inventory[index].get_rect())
        # (18 * index + 94, 18 * index + 94, 16, 16))

    def draw_surface(self) -> bool:
        logging.debug("draw inventory onto the screen")
        if not self._open:
            return False
        else:
            pygame.draw.rect(self.surface,
                             (128, 128, 128),
                             (90, 90, 400 - 90, 400 - 90)
                             )
            self.surface.set_alpha(200)
            for i in range(len(self.inventory)):
                self.draw_item(i)
            return True

    def set_open(self, state: bool):
        self._open = state

    def close_inventory(self):
        self.set_open(False)

    def is_full(self):
        return len(self.inventory) >= self.INV_MAX_LENGTH

    def insert_item(self, index: int, item: Items.baseItem.BaseItem) -> bool:
        if index >= self.INV_MAX_LENGTH:
            return False
        self.inventory.insert(index, item)
        self.inventory[index].update_location(index)
        return True

    def remove_item(self, index: int) -> bool:
        if len(self.inventory) >= index:
            self.inventory.pop(index)
            return True
        return False

    @main_hand.setter
    def main_hand(self, value):
        self._main_hand = value
