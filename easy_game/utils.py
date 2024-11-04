import random

from settings import *
import pygame


def get_lose_text_coord(lost_text) -> (int, int):
    return WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2


def show_lose_text(font, win):
    lost_text = font.render("You lost!", 1, "white")
    win.blit(lost_text, get_lose_text_coord(lost_text))
    pygame.display.update()
    pygame.time.delay(DELAY_TIME_AFTER_LOSING)


def draw_stars(stars, win):
    for star in stars:
        pygame.draw.rect(win, "white", star)


def generate_new_stars(stars):
    for _ in range(3):
        star_x = random.randint(0, WIDTH - STAR_WIDTH)
        star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
        stars.append(star)


