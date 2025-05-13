from abc import ABC, abstractmethod


class FlyStrategy(ABC):
    @abstractmethod
    def fly(self):
        """Strategy interface for implementing different flying behaviors."""
        pass
