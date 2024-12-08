from config import MAX_BULLETS
import pygame


class Spaceship(pygame.Rect):

    def __init__(self, x_coord: int, y_coord: int, *size: tuple[int, int]):
        super().__init__(x_coord, y_coord, *size)
        self.__x = x_coord
        self.__y = y_coord
        self.__width, self.__height = size
        self.__spaceship_bullets = []

    def valid_bullets_count(self) -> bool:
        return len(self.__spaceship_bullets) < MAX_BULLETS

    def handle_create_bullet(self, *, invert=False):
        if not invert:
            bullet = self.create_bullets_for_left_spaceship()
        else:
            bullet = self.create_bullets_for_right_spaceship()
        self.add_bullet(bullet)

    def add_bullet(self, bullet: pygame.Rect) -> None:
        if not isinstance(bullet, pygame.Rect):
            raise TypeError(f"Bullet should be type pygame.Rect, got{type(bullet)}")
        self.__spaceship_bullets.append(bullet)

    def create_bullets_for_left_spaceship(self) -> pygame.Rect:
        bullet = pygame.Rect(self.__x + self.__width, self.__y + self.__height / 2 - 2, 10, 5)
        return bullet

    def create_bullets_for_right_spaceship(self) -> pygame.Rect:
        bullet = pygame.Rect(self.__x, self.__y + self.__height / 2 - 2, 10, 5)
        return bullet

    def get_spaceship_bullets(self) -> list[pygame.Rect]:
        return self.__spaceship_bullets

    def get_x(self) -> int:
        return self.__x

    def set_x(self, val: int):
        if not isinstance(val, int):
            raise TypeError(f"coord must be int type, got {type(val)}")
        self.__x = val

    def get_y(self) -> int:
        return self.__y

    def set_y(self, val: int):
        if not isinstance(val, int):
            raise TypeError(f"coord must be int type, got {type(val)}")
        self.__y = val
