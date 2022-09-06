from models.Weapons.Weapon import Weapon


class Sword(Weapon):
    def get_attack_point(self) -> int:
        return 2

    def __str__(self) -> str:
        return "Espada"