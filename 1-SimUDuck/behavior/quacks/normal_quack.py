from ..quack_behavior import QuackBehavior


class NormalQuack(QuackBehavior):
    def quack(self):
        print("Quack!")
