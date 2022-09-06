from models.Events.PlayerDead import PlayerDead
from models.Monsters.Monster import Monster
from models.Weapons.Sword import Sword


class Player(Monster):

    def __init__(self, name: str):
        super().__init__(20, Sword(), name)

    def healing(self) -> None:
        self.actualHealt += 3
        if self.actualHealt > self.maxHealt:
            self.actualHealt = self.maxHealt

    def dead(self) -> None:
        self.observableEvent.on_next(PlayerDead())
        self.observableEvent.on_completed()