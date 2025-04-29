from abc import ABC, abstractmethod


class Quack(ABC):
    @abstractmethod
    def quack(self):
        pass
