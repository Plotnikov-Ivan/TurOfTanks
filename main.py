import pygame
import sys

# Инициализация Pygame
pygame.init()

# Устанавливаем ширину и высоту окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Туровские танки")

# Определяем цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 150, 0)
ORANGE = (255, 165, 0)
LIGHT_RED = (255, 100, 100, 100)


# Функция для загрузки стен из файла
def load_walls():
    try:
        with open("walls.txt", "r") as file:
            walls_data = file.readlines()
        walls = [list(map(int, wall.strip().split())) for wall in walls_data]
        return walls
    except FileNotFoundError:
        return []


# Загрузка координат стен
walls = load_walls()

# Переменные для хранения координат последнего квадрата и круга
last_square = None
# Переменная для хранения круга
last_circle = None

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Убираем предыдущий квадрат и круг
            if last_square:
                pygame.draw.rect(screen, BLACK, last_square)
            if last_circle:
                pygame.draw.circle(screen, BLACK, last_circle.center, 100)  # Удаляем предыдущий круг

            mouse_pos = pygame.mouse.get_pos()
            square_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 50, 50)

            circle_radius = 100
            circle_center = (square_rect.centerx, square_rect.centery)
            pygame.draw.circle(screen, LIGHT_RED, circle_center, circle_radius)
            last_circle = pygame.Rect(square_rect.centerx - circle_radius, square_rect.centery - circle_radius, circle_radius * 2, circle_radius * 2)
            pygame.draw.rect(screen, GREEN, square_rect)

            # Рисуем прямоугольники
            smaller_edge = 25
            rectangle_rect = pygame.Rect(
                square_rect.x + (square_rect.width - smaller_edge) // 2,
                square_rect.y + (square_rect.height - smaller_edge) // 2,
                smaller_edge,
                smaller_edge
            )
            pygame.draw.rect(screen, DARK_GREEN, rectangle_rect)

            edge = 12
            rectangle_rect = pygame.Rect(
                square_rect.x + (square_rect.width - edge) // 2,
                square_rect.y + (square_rect.height - edge) // 2 - 19,
                edge,
                edge
            )
            pygame.draw.rect(screen, DARK_GREEN, rectangle_rect)

            last_square = square_rect

            # Рисуем стены
            for wall_data in walls:
                wall_rect = pygame.Rect(wall_data[0], wall_data[1], 70, 70)
                pygame.draw.rect(screen, ORANGE, wall_rect)

    for wall_data in walls:
        wall_rect = pygame.Rect(wall_data[0], wall_data[1], 70, 70)
        pygame.draw.rect(screen, ORANGE, wall_rect)

    # Обновление экрана
    pygame.display.flip()