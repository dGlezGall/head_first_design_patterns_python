from behavior import FlyBehavior, FlyNoWay, QuackBehavior, MuteQuack
from duck import BaseDuck


class DecoyDuck(BaseDuck):
    def __init__(self, fb: FlyBehavior = FlyNoWay(), qb: QuackBehavior = MuteQuack()):
        super()
        self.fly_behavior = fb
        self.quack_behavior = qb

    def display(self):
        print("I am a Decoy Duck!")
