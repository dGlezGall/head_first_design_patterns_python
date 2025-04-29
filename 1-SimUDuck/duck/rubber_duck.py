from behavior import FlyBehavior, FlyNoWay, QuackBehavior, SqueakQuack
from .duck import Duck


class RubberDuck(Duck):
    def __init__(self, fb: FlyBehavior = FlyNoWay(), qb: QuackBehavior = SqueakQuack()):
        super().__init__(fb, qb)

    def display(self):
        print("I am a Rubber Duck!")
