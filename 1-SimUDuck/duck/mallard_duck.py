from behavior import Fly, FlyWithWings, Quack, NormalQuack
from .duck import Duck


class MallardDuck(Duck):

    def __init__(self, fb: Fly = FlyWithWings(), qb: Quack = NormalQuack()):
        super().__init__(fb, qb)

    def display(self):
        print("I am a Mallard Duck!")
