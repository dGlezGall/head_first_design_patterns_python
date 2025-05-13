from ..fly import FlyStrategy


class FlyNoWay(FlyStrategy):
    def fly(self):
        print("I can't fly! :(")
