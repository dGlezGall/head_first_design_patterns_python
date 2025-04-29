from behavior.fly import FlyBehavior, FlyWithWings
from behavior.quack import QuackBehavior, Quack
from duck.base_duck import Duck


class MallardDuck(Duck):

    def __init__(self, fb: FlyBehavior = FlyWithWings(), qb: QuackBehavior = Quack()):
        super()
        self.fly_behavior = fb
        self.quack_behavior = qb

    def display(self):
        print("I am a Mallard Duck!")
