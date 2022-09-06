import abc
import typing

from rx.subject import Subject

from models.Events.MonsterDead import MonsterDead

if typing.TYPE_CHECKING:
    from models.Weapons.Weapon import Weapon
    from models.Events.Event import Event

class Monster(metaclass=abc.ABCMeta):

    def __init__(self,
                 maxHealt: int,
                 weapon: 'Weapon',
                 name: str):
        self.maxHealt = maxHealt
        self.equipedWeapon = weapon
        self.name = name
        self.actualHealt = maxHealt
        self.observableEvent: Subject['Event'] = Subject()

    def get_attack_point(self) -> int:
        return self.equipedWeapon.get_attack_point()

    def take_damage(self, monster: 'Monster') -> None:
        self.actualHealt -= monster.get_attack_point()
        if self.actualHealt <= 0:
            self.actualHealt = 0
            self.dead()

    def attack(self, target: 'Monster') -> None:
        target.take_damage(self)

    def dead(self) -> None:
        self.observableEvent.on_next(MonsterDead())
        self.observableEvent.on_completed()