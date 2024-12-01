import pygame

from config import *
from services import (handle_yellow_key_pressed, handle_red_key_pressed, handle_create_bullet,
                      valid_bullets_count)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("First Game!")


def draw_window(red, yellow):
    WIN.fill(WHITE_COLOR)
    pygame.draw.rect(WIN, BLACK_COLOR, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def main():
    red = pygame.Rect(RED_SPACESHIP_X, RED_SPACESHIP_Y, *RED_SPACESHIP_RESIZE_SIZE)
    yellow = pygame.Rect(YELLOW_SPACESHIP_X, YELLOW_SPACESHIP_Y, *YELLOW_SPACESHIP_RESIZE_SIZE)

    red_spaceship_bullets = []
    yellow_spaceship_bullets = []

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and valid_bullets_count(yellow_spaceship_bullets):
                    bullet = handle_create_bullet(yellow)
                    yellow_spaceship_bullets.append(bullet)

                if event.type == pygame.K_RCTRL and valid_bullets_count(red_spaceship_bullets):
                    bullet = handle_create_bullet(red, invert=True)
                    red_spaceship_bullets.append(bullet)

        print(red_spaceship_bullets, yellow_spaceship_bullets)
        keys_pressed = pygame.key.get_pressed()
        handle_yellow_key_pressed(keys_pressed, yellow)
        handle_red_key_pressed(keys_pressed, red)
        draw_window(red, yellow)
    pygame.quit()


if __name__ == "__main__":
    main()
