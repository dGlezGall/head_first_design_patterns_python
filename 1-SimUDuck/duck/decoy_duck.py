from behavior import FlyBehavior, FlyNoWay, QuackBehavior, MuteQuack
from .duck import Duck


class DecoyDuck(Duck):
    def __init__(self, fb: FlyBehavior = FlyNoWay(), qb: QuackBehavior = MuteQuack()):
        super().__init__(fb, qb)

    def display(self):
        print("I am a Decoy Duck!")
