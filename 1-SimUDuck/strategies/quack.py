from abc import ABC, abstractmethod


class QuackStrategy(ABC):
    @abstractmethod
    def quack(self):
        """Strategy interface for implementing different quacking behaviors."""
        pass
