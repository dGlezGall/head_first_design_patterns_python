from behavior.fly import FlyBehavior, FlyNoWay
from behavior.quack import QuackBehavior, Squeak
from duck.base_duck import Duck


class RubberDuck(Duck):
    def __init__(self, fb: FlyBehavior = FlyNoWay(), qb: QuackBehavior = Squeak()):
        super()
        self.fly_behavior = fb
        self.quack_behavior = qb

    def display(self):
        print("I am a Rubber Duck!")
