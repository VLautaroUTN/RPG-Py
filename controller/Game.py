import typing

from rx.subject import Subject

from models.Monsters.Goblin import Goblin

if typing.TYPE_CHECKING:
    from models.Monsters.Player import Player
    from models.Events.Event import Event

class Game:

    def __init__(self, gamer: 'Player'):
        self.gamer = gamer
        self.actualmonster = Goblin()
        self.monsterlist = [
            Goblin(),
            Goblin()
        ]

        self.gamerDisposable = self.gamer.observableEvent.subscribe()      #Pendiente
        self.actualMonsterDisposable = \
            self.actualmonster.observableEvent.subscribe()      #Pendiente

        self.result: Subject[bool] = Subject()
        self.nextMonsterName: Subject[str] = Subject()

    def clearMemory(self) -> None:
        self.gamerDisposable.dispose()
        self.actualMonsterDisposable.dispose()

    def win(self) -> None:
        self.clearMemory()
        self.result.on_next(True)
        self.result.on_completed()

    def loss(self) -> None:
        self.clearMemory()
        self.result.on_next(False)
        self.result.on_completed()

    def aceptEvent(self,event: 'Event') -> None:
        pass