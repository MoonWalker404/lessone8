import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SIZE = 50
ENEMY_SIZE = 50
ENEMY_SPAWN_RATE = 30  # Количество кадров до появления нового врага

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Окно игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survival Game")

# Классы
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
        self.color = GREEN

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        # Ограничение движения игрока по границам окна
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Enemy:
    def __init__(self):
        x = random.randint(0, WIDTH - ENEMY_SIZE)
        y = random.randint(0, HEIGHT - ENEMY_SIZE)
        self.rect = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)
        self.color = RED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Функция для проверки столкновений
def check_collision(player, enemies):
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            return True
    return False

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()
    player = Player()
    enemies = []
    frames = 0

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -5
        if keys[pygame.K_RIGHT]:
            dx = 5
        if keys[pygame.K_UP]:
            dy = -5
        if keys[pygame.K_DOWN]:
            dy = 5
        player.move(dx, dy)

        # Появление новых врагов
        frames += 1
        if frames % ENEMY_SPAWN_RATE == 0:
            enemies.append(new_enemy := Enemy())

        # Проверка столкновений
        if check_collision(player, enemies):
            print("Game Over!")
            running = False

        # Отрисовка
        screen.fill(WHITE)
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
# Очень интересно но ничего не понятно)