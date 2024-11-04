import os

import pygame

from config import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets", "spaceship_yellow.png"))
pygame.display.set_caption("First Game!")


def draw_window():
    WIN.fill(WHITE_COLOR)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
