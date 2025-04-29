from behavior import FlyBehavior, FlyWithWings, QuackBehavior, NormalQuack
from .duck import Duck


class MallardDuck(Duck):

    def __init__(self, fb: FlyBehavior = FlyWithWings(), qb: QuackBehavior = NormalQuack()):
        super().__init__(fb, qb)

    def display(self):
        print("I am a Mallard Duck!")
