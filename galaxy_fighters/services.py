import pygame

from spaceship import Spaceship
from spaceship_moving import SpaceshipMoving
from config import VELOCITY, BORDER, HEIGHT, WIDTH, BULLET_VELOCITY

ADD_BORDER_PIXELS = 10  # Додаткові пікселі знизу і справа від розмежувального контейнеру,
# щоб корабель не входив у межу екрану


def can_move_left(spaceship: Spaceship, *, invert=False) -> bool:
    if not invert:
        return spaceship.get_x() - VELOCITY > 0
    return spaceship.get_x() - VELOCITY > BORDER.x + ADD_BORDER_PIXELS + BORDER.width


def can_move_right(spaceship: Spaceship, *, invert=False) -> bool:
    if not invert:
        return spaceship.get_x() + VELOCITY + spaceship.width < BORDER.x
    return spaceship.get_x() + VELOCITY + spaceship.width < WIDTH


def can_move_top(spaceship: Spaceship) -> bool:
    return spaceship.get_y() - VELOCITY > 0


def can_move_bottom(spaceship: Spaceship) -> bool:
    return spaceship.get_y() + VELOCITY + spaceship.height < HEIGHT - ADD_BORDER_PIXELS


def handle_yellow_key_pressed(keys_pressed, yellow: Spaceship):
    moving = SpaceshipMoving(yellow=yellow)
    if keys_pressed[pygame.K_a] and can_move_left(yellow):
        moving.moving_left(yellow)
    elif keys_pressed[pygame.K_d] and can_move_right(yellow):
        moving.moving_right(yellow)
    elif keys_pressed[pygame.K_w] and can_move_top(yellow):
        moving.moving_top(yellow)
    elif keys_pressed[pygame.K_s] and can_move_bottom(yellow):
        moving.moving_bottom(yellow)


def handle_red_key_pressed(keys_pressed, red: Spaceship):
    moving = SpaceshipMoving(red=red)
    if keys_pressed[pygame.K_LEFT] and can_move_left(red, invert=True):
        moving.moving_left(red)
    elif keys_pressed[pygame.K_RIGHT] and can_move_right(red, invert=True):
        moving.moving_right(red)
    elif keys_pressed[pygame.K_UP] and can_move_top(red):
        moving.moving_top(red)
    elif keys_pressed[pygame.K_DOWN] and can_move_bottom(red):
        moving.moving_bottom(red)


def handle_bullets(yellow_bullets: list[pygame.Rect], red_bullets: list[pygame.Rect],
                   yellow: Spaceship, red: Spaceship):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY

        if yellow.colliderect(bullet):
            ...
