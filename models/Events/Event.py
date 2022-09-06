import abc


class Event(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def start_event(self):
        pass