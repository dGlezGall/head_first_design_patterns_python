from behavior import Fly, FlyRocketPowered
from ducks import DecoyDuck, MallardDuck, RubberDuck


if __name__ == "__main__":
    print("======= SimUDuck =======")

    print("-------")
    print("Mallard Duck:")
    mallard = MallardDuck()
    mallard.display()
    mallard.swim()
    mallard.perform_quack()
    mallard.perform_fly()

    print("-------")
    print("Decoy Duck:")
    decoy = DecoyDuck()
    decoy.display()
    decoy.swim()
    decoy.perform_quack()
    decoy.perform_fly()

    print("-------")
    print("Rubber Duck:")
    rubber = RubberDuck()
    rubber.display()
    rubber.swim()
    rubber.perform_quack()
    rubber.perform_fly()
    fly_with_rocket: Fly = FlyRocketPowered()
    rubber.set_fly_behavior(fly_with_rocket)
    rubber.perform_fly()
