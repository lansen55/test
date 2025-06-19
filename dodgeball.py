"""A simple dodgeball game implemented with Pygame."""

import random
try:
    import pygame
except ImportError:  # pragma: no cover - for environments without pygame
    raise SystemExit(
        "pygame is required to run this game."
        " Install with 'pip install pygame' or run ./setup_env.sh"
    )


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = (50, 50)
BALL_SIZE = (30, 30)
BALL_COUNT = 5


def main() -> None:
    """Run the dodgeball game loop."""

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dodgeball")
    clock = pygame.time.Clock()

    player = pygame.Rect(
        (SCREEN_WIDTH - PLAYER_SIZE[0]) // 2,
        SCREEN_HEIGHT - 100,
        *PLAYER_SIZE,
    )

    balls = [
        pygame.Rect(
            random.randint(0, SCREEN_WIDTH - BALL_SIZE[0]),
            random.randint(-500, -BALL_SIZE[1]),
            *BALL_SIZE,
        )
        for _ in range(BALL_COUNT)
    ]
    ball_speeds = [random.randint(3, 7) for _ in range(BALL_COUNT)]

    font = pygame.font.Font(None, 36)
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= 6
        if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
            player.x += 6

        for idx, ball in enumerate(balls):
            ball.y += ball_speeds[idx]
            if ball.top > SCREEN_HEIGHT:
                ball.x = random.randint(0, SCREEN_WIDTH - BALL_SIZE[0])
                ball.y = random.randint(-100, -BALL_SIZE[1])
                ball_speeds[idx] = random.randint(3, 7)
                score += 1

            if player.colliderect(ball):
                running = False

        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, (0, 128, 255), player)
        for ball in balls:
            pygame.draw.ellipse(screen, (255, 0, 0), ball)

        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    end_font = pygame.font.Font(None, 72)
    over_surf = end_font.render("Game Over!", True, (255, 255, 255))
    screen.blit(
        over_surf,
        ((SCREEN_WIDTH - over_surf.get_width()) // 2, SCREEN_HEIGHT // 2 - 36),
    )
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()


if __name__ == "__main__":
    main()
