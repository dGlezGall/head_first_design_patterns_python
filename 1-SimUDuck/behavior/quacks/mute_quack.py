from ..quack import Quack


class MuteQuack(Quack):
    def quack(self):
        print("...")
