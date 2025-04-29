from abc import ABC, abstractmethod


class Fly(ABC):
    @abstractmethod
    def fly(self):
        pass
