import typing

from models.Monsters.Goblin import Goblin

if typing.TYPE_CHECKING:
    from models.Monsters.Monster import Monster


def take_damage_test(attackermonster: 'Monster'):
    goblin = Goblin()
    initHealt = goblin.actualHealt
    goblin.observableEvent.subscribe(
        lambda event: print(event),
    )
    for _ in range(3):
        attackermonster.attack(goblin)

    assert goblin.actualHealt < initHealt
    assert goblin.actualHealt == 0


def test():
    take_damage_test(Goblin())
    return None
