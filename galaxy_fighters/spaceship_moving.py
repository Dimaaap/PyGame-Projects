from config import *
from custom_errors import *


class SpaceshipMoving:

    def __init__(self, yellow=None, red=None):
        self.__yellow = yellow
        self.__red = red

    def moving_left(self, spaceship):
        if spaceship == "yellow":
            self.__yellow.x -= VELOCITY
        elif spaceship == "red":
            self.__red.x -= VELOCITY
        else:
            raise InvalidSpaceshipException("Wrong type of spaceship")

    def moving_right(self, spaceship):
        if spaceship == "yellow":
            self.__yellow.x += VELOCITY
        elif spaceship == "red":
            self.__red.x += VELOCITY
        else:
            raise InvalidSpaceshipException("Wrong type of spaceship")

    def moving_top(self, spaceship):
        if spaceship == "yellow":
            self.__yellow.y -= VELOCITY
        elif spaceship == "red":
            self.__red.y -= VELOCITY
        else:
            raise InvalidSpaceshipException("Wrong type of spaceship")

    def moving_bottom(self, spaceship):
        if spaceship == "yellow":
            self.__yellow.y += VELOCITY
        elif spaceship == "red":
            self.__red.y += VELOCITY
        else:
            raise InvalidSpaceshipException("Wrong type of spaceship")

