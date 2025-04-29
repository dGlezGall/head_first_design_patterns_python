from .fly_behavior import FlyBehavior
from .flights import FlyNoWay, FlyRocketPowered, FlyWithWings
from .quack_behavior import QuackBehavior
from .quacks import MuteQuack, SqueakQuack, NormalQuack

__all__ = [
    'FlyBehavior', 'FlyNoWay', 'FlyRocketPowered', 'FlyWithWings',
    'QuackBehavior', 'MuteQuack', 'SqueakQuack', 'NormalQuack'
]
