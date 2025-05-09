from pygame import *
import pygame
import random

pygame.init()
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Snake Game")
clock = pygame.time.Clock()

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


snake = [[5, 10], [5, 9], [5, 8]]
direction = "RIGHT"
food = [random.randint(0, WIDTH // GRID_SIZE - 1), random.randint(0, HEIGHT // GRID_SIZE - 1)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_d and direction != "LEFT":
                direction = "RIGHT"
            elif event.key == pygame.K_w and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_s and direction != "UP":
                direction = "DOWN"

      
    head = snake[0].copy()
    if direction == "RIGHT":
        head[1] += 1
    elif direction == "LEFT":
        head[1] -= 1
    elif direction == "UP":
        head[0] -= 1
    elif direction == "DOWN":
        head[0] += 1

    
    if (
        head in snake[1:]
        or head[0] < 0
        or head[0] >= HEIGHT // GRID_SIZE
        or head[1] < 0
        or head[1] >= WIDTH // GRID_SIZE
    ):
        running = False

    snake.insert(0, head)
    if head == food:
        food = [random.randint(0, WIDTH // GRID_SIZE - 1), random.randint(0, HEIGHT // GRID_SIZE - 1)]
    else:
        snake.pop()

    
    window.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(window, GREEN, (segment[1] * GRID_SIZE, segment[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(window, RED, (food[1] * GRID_SIZE, food[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    display.update()
    clock.tick(10) 

pygame.quit()