from abc import ABC, abstractmethod

from behavior import Fly, Quack


class Duck(ABC):

    def __init__(self, fb: Fly, qb: Quack):
        self.fly_behavior: Fly = fb
        self.quack_behavior: Quack = qb

    def swim(self):
        print("All ducks can swim")

    @abstractmethod
    def display(self):
        pass

    def set_fly_behavior(self, fb: Fly):
        self.fly_behavior = fb

    def perform_fly(self):
        self.fly_behavior.fly()

    def set_quack_behavior(self, qb: Quack):
        self.quack_behavior = qb

    def perform_quack(self):
        self.quack_behavior.quack()
