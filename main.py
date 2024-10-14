import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создаем окно
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра Тир')

# Иконка и цель
icon = pygame.image.load('img/4169771.jpg')
pygame.display.set_icon(icon)

target_image = pygame.image.load('img/target.png')
target_width = target_image.get_width()
target_height = target_image.get_height()
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Счётчик попаданий
score = 0
font = pygame.font.Font(None, 36)

# Таймер для смены положения мишени каждые 3 секунды (3000 миллисекунд)
TARGET_MOVE_EVENT = pygame.USEREVENT + 1
initial_target_timer = 3000  # начальный интервал в миллисекундах
min_target_timer = 500  # минимальный интервал (0.5 секунд)
current_target_timer = initial_target_timer
pygame.time.set_timer(TARGET_MOVE_EVENT, current_target_timer)

# Основной игровой цикл
running = True
while running:
    # Заливаем экран цветом
    screen.fill(color)

    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверяем попадание в цель
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Увеличиваем счётчик
                score += 1
                # Перемещаем цель на новое случайное место
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

                # Ускоряем перемещение мишени каждые 20 попаданий
                if score % 20 == 0:
                    # Уменьшаем таймер на 20%
                    current_target_timer = max(int(current_target_timer * 0.8), min_target_timer)

                pygame.time.set_timer(TARGET_MOVE_EVENT, current_target_timer)

        # Проверяем таймер для смены положения мишени
        if event.type == TARGET_MOVE_EVENT:
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Отрисовываем цель
    screen.blit(target_image, (target_x, target_y))

    # Отображаем счёт
    score_text = font.render(f"Счёт: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Обновляем экран
    pygame.display.update()

# Выход из Pygame
pygame.quit()
