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
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = SCREEN_HEIGHT - 40
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        if direction == "right" and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

    def reset(self):
        self.rect.x = (SCREEN_WIDTH - self.width) // 2

class Ball:
    def __init__(self):
        self.radius = 10
        self.reset()

    def reset(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x = random.choice([-5, 5])
        self.speed_y = -5
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def update(self, paddle, blocks):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Столкновение с краями экрана
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y

        # Столкновение с платформой
        if self.rect.colliderect(paddle.rect):
            self.speed_y = -self.speed_y

        # Столкновение с блоками
        for block in blocks:
            if self.rect.colliderect(block.rect):
                blocks.remove(block)
                self.speed_y = -self.speed_y
                break

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)

def create_blocks():
    return [Block(x * 70 + 10, y * 30 + 10) for x in range(10) for y in range(5)]

class Block:
    def __init__(self, x, y):
        self.width = 60
        self.height = 20
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Арканоид")

    clock = pygame.time.Clock()

    paddle = Paddle()
    ball = Ball()

    blocks = create_blocks()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move("left")
        if keys[pygame.K_RIGHT]:
            paddle.move("right")

        ball.update(paddle, blocks)

        if ball.rect.bottom >= SCREEN_HEIGHT:
            ball.reset()
            paddle.reset()
            blocks = create_blocks()  # Сбрасываем блоки при пропуске шарика

        screen.fill(BLACK)
        paddle.draw(screen)
        ball.draw(screen)
        for block in blocks:
            block.draw(screen)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
