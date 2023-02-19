class Stat:

    def __init__(self, health: int):
        self._health = health

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @health.deleter
    def health(self):
        self._health = 0
