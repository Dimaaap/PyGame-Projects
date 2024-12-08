from config import *
from custom_errors import *
from spaceship import Spaceship


class SpaceshipMoving:

    def __init__(self, yellow=None, red=None):
        self.__yellow = yellow
        self.__red = red

    def moving_left(self, spaceship: Spaceship):
        if isinstance(spaceship, Spaceship):
            new_coord = spaceship.get_x() - VELOCITY
            spaceship.set_x(new_coord)
        else:
            raise InvalidSpaceshipException("Wrong type of spaceship")

    def moving_right(self, spaceship: Spaceship):
        if isinstance(spaceship, Spaceship):
            new_coord = spaceship.get_x() + VELOCITY
            spaceship.set_x(new_coord)
        else:
            raise InvalidSpaceshipException("Wrong type of spaceship")

    def moving_top(self, spaceship: Spaceship):
        if isinstance(spaceship, Spaceship):
            new_coord = spaceship.get_y() - VELOCITY
            spaceship.set_y(new_coord)
        else:
            raise InvalidSpaceshipException("Wrong type of spaceship")

    def moving_bottom(self, spaceship):
        if isinstance(spaceship, Spaceship):
            new_coord = spaceship.get_y() + VELOCITY
            spaceship.set_y(new_coord)
        else:
            raise InvalidSpaceshipException("Wrong type of spaceship")
