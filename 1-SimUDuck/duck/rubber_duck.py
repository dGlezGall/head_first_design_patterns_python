from behavior import FlyBehavior, FlyNoWay, QuackBehavior, Squeak
from duck import BaseDuck


class RubberDuck(BaseDuck):
    def __init__(self, fb: FlyBehavior = FlyNoWay(), qb: QuackBehavior = Squeak()):
        super()
        self.fly_behavior = fb
        self.quack_behavior = qb

    def display(self):
        print("I am a Rubber Duck!")
