from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I am flying with wings!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly! :(")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I am flying on A ROCKET! :D")
