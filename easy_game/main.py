import time

from utils import *

pygame.font.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("easy_game/bg.jpeg"), (WIDTH, HEIGHT))

FONT = pygame.font.SysFont("comicsans", 30)


def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)
    draw_stars(stars, WIN)
    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()

    start_add_increment = 2_000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(FPS)
        elapsed_time = time.time() - start_time

        if star_count > start_add_increment:
            generate_new_stars(stars)
            start_add_increment = max(200, start_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            show_lose_text(FONT, WIN)
            break
        draw(player, elapsed_time, stars)
    pygame.quit()


if __name__ == "__main__":
    main()
