from .fly import FlyStrategy
from .flights import FlyNoWay, FlyRocketPowered, FlyWithWings
from .quack import QuackStrategy
from .quacks import MuteQuack, SqueakQuack, NormalQuack

__all__ = [
    'FlyStrategy', 'FlyNoWay', 'FlyRocketPowered', 'FlyWithWings',
    'QuackStrategy', 'MuteQuack', 'SqueakQuack', 'NormalQuack'
]
