import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Paddle:
    def __init__(self, x, y):
        self.width = 100
        self.height = 10
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.speed = 10

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        if direction == "right" and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y


class Ball:
    def __init__(self):
        self.radius = 10
        self.reset()

    def reset(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - self.radius, SCREEN_HEIGHT // 2 - self.radius, self.radius * 2,
                                self.radius * 2)
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-5, 5])

    def update(self, paddle1, paddle2):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Столкновение с краями экрана
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x

        # Столкновение с платформами
        if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
            self.speed_y = -self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Пинг-Понг")

    clock = pygame.time.Clock()

    paddle1 = Paddle((SCREEN_WIDTH - 100) // 2, SCREEN_HEIGHT - 30)
    paddle2 = Paddle((SCREEN_WIDTH - 100) // 2, 20)
    ball = Ball()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle1.move("left")
        if keys[pygame.K_RIGHT]:
            paddle1.move("right")
        if keys[pygame.K_a]:
            paddle2.move("left")
        if keys[pygame.K_d]:
            paddle2.move("right")

        ball.update(paddle1, paddle2)

        # Проверка на пропуск шарика
        if ball.rect.top <= 0 or ball.rect.bottom >= SCREEN_HEIGHT:
            ball.reset()
            paddle1.reset((SCREEN_WIDTH - 100) // 2, SCREEN_HEIGHT - 30)
            paddle2.reset((SCREEN_WIDTH - 100) // 2, 20)

        screen.fill(BLACK)
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
