from ..quack import QuackStrategy


class MuteQuack(QuackStrategy):
    def quack(self):
        print("...")
