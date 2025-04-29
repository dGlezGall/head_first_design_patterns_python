from abc import abstractmethod

from behavior.fly import FlyBehavior
from behavior.quack import QuackBehavior


class Duck():

    def __init__(self, fb: FlyBehavior, qb: QuackBehavior):
        self.fly_behavior: FlyBehavior = fb
        self.quack_behavior: QuackBehavior = qb

    def swim(self):
        print("All ducks can swim")

    @abstractmethod
    def display(self):
        pass

    def set_fly_behavior(self, fb: FlyBehavior):
        self.fly_behavior = fb

    def perform_fly(self):
        self.fly_behavior.fly()

    def set_quack_behavior(self, qb: QuackBehavior):
        self.quack_behavior = qb

    def perform_quack(self):
        self.quack_behavior.quack()
