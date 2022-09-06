import abc


class Weapon(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_attack_point(self) -> int:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass
