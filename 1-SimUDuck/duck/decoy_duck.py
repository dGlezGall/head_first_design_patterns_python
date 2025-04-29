from behavior.fly import FlyBehavior, FlyNoWay
from behavior.quack import QuackBehavior, MuteQuack
from duck.base_duck import Duck


class DecoyDuck(Duck):
    def __init__(self, fb: FlyBehavior = FlyNoWay(), qb: QuackBehavior = MuteQuack()):
        super()
        self.fly_behavior = fb
        self.quack_behavior = qb

    def display(self):
        print("I am a Decoy Duck!")
