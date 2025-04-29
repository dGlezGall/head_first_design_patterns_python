from behavior import Fly, FlyNoWay, Quack, SqueakQuack
from .duck import Duck


class RubberDuck(Duck):
    def __init__(self, fb: Fly = FlyNoWay(), qb: Quack = SqueakQuack()):
        super().__init__(fb, qb)

    def display(self):
        print("I am a Rubber Duck!")
