from strategies import FlyStrategy, FlyNoWay, QuackStrategy, SqueakQuack
from .duck import Duck


class RubberDuck(Duck):
    def __init__(self, fly_strategy: FlyStrategy = FlyNoWay(), quack_strategy: QuackStrategy = SqueakQuack()):
        super().__init__(
            fly_strategy=fly_strategy,
            quack_strategy=quack_strategy
        )

    def display(self):
        print("I am a Rubber Duck!")
