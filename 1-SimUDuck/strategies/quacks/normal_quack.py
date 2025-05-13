from ..quack import QuackStrategy


class NormalQuack(QuackStrategy):
    def quack(self):
        print("Quack!")
