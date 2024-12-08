from config import *
from services import (handle_yellow_key_pressed, handle_red_key_pressed, handle_bullets)
from spaceship import Spaceship

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("First Game!")


def draw_window(red: Spaceship, yellow: Spaceship):
    WIN.fill(WHITE_COLOR)
    pygame.draw.rect(WIN, BLACK_COLOR, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.get_x(), yellow.get_y()))
    WIN.blit(RED_SPACESHIP, (red.get_x(), red.get_y()))
    pygame.display.update()


def main():
    red = Spaceship(RED_SPACESHIP_X, RED_SPACESHIP_Y, *RED_SPACESHIP_RESIZE_SIZE)
    yellow = Spaceship(YELLOW_SPACESHIP_X, YELLOW_SPACESHIP_Y, *YELLOW_SPACESHIP_RESIZE_SIZE)

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and yellow.valid_bullets_count():
                    yellow.handle_create_bullet()

                if event.key == pygame.K_RCTRL and red.valid_bullets_count():
                    red.handle_create_bullet(invert=True)

        keys_pressed = pygame.key.get_pressed()
        handle_yellow_key_pressed(keys_pressed, yellow)
        handle_red_key_pressed(keys_pressed, red)
        handle_bullets(yellow.get_spaceship_bullets(), red.get_spaceship_bullets(), yellow, red)
        draw_window(red, yellow)
    pygame.quit()


if __name__ == "__main__":
    main()
