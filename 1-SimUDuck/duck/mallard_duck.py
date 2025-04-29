from behavior import FlyBehavior, FlyWithWings, QuackBehavior, Quack
from duck import BaseDuck


class MallardDuck(BaseDuck):

    def __init__(self, fb: FlyBehavior = FlyWithWings(), qb: QuackBehavior = Quack()):
        super()
        self.fly_behavior = fb
        self.quack_behavior = qb

    def display(self):
        print("I am a Mallard Duck!")
