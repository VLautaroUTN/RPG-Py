from models.Monsters.Monster import Monster
from models.Weapons.Sword import Sword


class Goblin(Monster):

    def __init__(self):
        super().__init__(5, Sword(), "Goblin")