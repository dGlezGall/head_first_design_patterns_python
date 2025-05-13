from abc import ABC, abstractmethod

from strategies import FlyStrategy, QuackStrategy


class Duck(ABC):

    def __init__(self, fly_strategy: FlyStrategy, quack_strategy: QuackStrategy):
        self.fly_strategy: FlyStrategy = fly_strategy
        self.quack_strategy: QuackStrategy = quack_strategy

    def swim(self):
        print("All ducks can swim")

    @abstractmethod
    def display(self):
        pass

    def set_fly_strategy(self, fb: FlyStrategy):
        self.fly_strategy = fb

    def perform_fly(self):
        self.fly_strategy.fly()

    def set_quack_strategy(self, qb: QuackStrategy):
        self.quack_strategy = qb

    def perform_quack(self):
        self.quack_strategy.quack()
