from strategies import FlyStrategy, FlyWithWings, QuackStrategy, NormalQuack
from .duck import Duck


class MallardDuck(Duck):

    def __init__(self, fly_strategy: FlyStrategy = FlyWithWings(), quack_strategy: QuackStrategy = NormalQuack()):
        super().__init__(
            fly_strategy=fly_strategy,
            quack_strategy=quack_strategy
        )

    def display(self):
        print("I am a Mallard Duck!")
