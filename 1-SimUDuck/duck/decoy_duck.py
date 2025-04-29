from behavior import Fly, FlyNoWay, Quack, MuteQuack
from .duck import Duck


class DecoyDuck(Duck):
    def __init__(self, fb: Fly = FlyNoWay(), qb: Quack = MuteQuack()):
        super().__init__(fb, qb)

    def display(self):
        print("I am a Decoy Duck!")
