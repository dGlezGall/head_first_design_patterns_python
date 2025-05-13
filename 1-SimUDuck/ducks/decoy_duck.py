from strategies import FlyStrategy, FlyNoWay, QuackStrategy, MuteQuack
from .duck import Duck


class DecoyDuck(Duck):
    def __init__(self, fly_strategy: FlyStrategy = FlyNoWay(), quack_strategy: QuackStrategy = MuteQuack()):
        super().__init__(
            fly_strategy=fly_strategy,
            quack_strategy=quack_strategy
        )

    def display(self):
        print("I am a Decoy Duck!")
