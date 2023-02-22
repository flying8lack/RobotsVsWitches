from NPC.Enemy.AbstractEnemy import AbstractEnemy
from battle.BattleScreen import BattleScreen
from util.player import Player


class Battle:

    def __init__(self, player: Player, enemy: AbstractEnemy):
        self.screen = BattleScreen(player, enemy)
        self.battle_ended = False
        self.player_turn = False

    def _change_turn(self) -> None:
        self.player_turn = not self.player_turn

    def is_player_turn(self) -> bool:
        return self.player_turn

    def event_handle(self):
        pass



    def draw(self):
        pass
