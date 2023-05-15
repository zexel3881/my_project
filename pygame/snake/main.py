import pygame
from random import randint
import draw_background
import control_snake
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
)

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([660, 700])
pygame.display.set_caption('snake')
clock = pygame.time.Clock()
FPS = 60  # frame per second, also relating with game speed, default = 60


def start():
    global move_x, move_y, move_speed, direction, snake, past_snake, spawn_fruit, fruit_x, fruit_y, score
    move_x, move_y = 1, 0
    move_speed = 5
    direction = [1]
    snake = [[75, 45], [70, 45], [65, 45], [60, 45], [60, 45], [55, 45], [50, 45],]
    past_snake = [[75, 45], [70, 45], [65, 45], [60, 45], [60, 45], [55, 45], [50, 45],]
    spawn_fruit = 0
    fruit_x = 45 + 30 * randint(0, 19)
    fruit_y = 45 + 30 * randint(0, 19)
    score = 0


start()

# Run until the user asks to quit
running = True
while running:
    screen.fill((255, 255, 255))
    clock.tick(FPS)

    for event in pygame.event.get():
        # when you clik quit out button, this code make you go out
        if event.type == pygame.QUIT:
            running = False
            break

        # change snake's moving direction
        if event.type == KEYDOWN:
            if event.key == K_RIGHT and direction[0] != 3:
                direction[0] = 1
            if event.key == K_UP and direction[0] != 4:
                direction[0] = 2
            if event.key == K_LEFT and direction[0] != 1:
                direction[0] = 3
            if event.key == K_DOWN and direction[0] != 2:
                direction[0] = 4

    # change snake's moving direction
    if (snake[0][0] - 15) % 30 == 0 and (snake[0][1] - 15) % 30 == 0:
        move_x, move_y = control_snake.change_direction(direction[0])

    # draw background pattern
    draw_background.background(screen)

    # spawn fruit
    if spawn_fruit == 1:
        while True:
            fruit_x = 45 + 30 * randint(0, 19)
            fruit_y = 45 + 30 * randint(0, 19)

            if [fruit_x, fruit_y] not in snake:
                break

        # when snake eat fruit, make snake be long
        for i in range(6):
            snake.append([-100, -100])
            past_snake.append([0, 0])

        spawn_fruit = 0

    pygame.draw.circle(screen, (255, 0, 0), (fruit_x,  fruit_y), 13)

    # check whether snake eat a fruit
    if fruit_x == snake[0][0] and fruit_y == snake[0][1]:
        spawn_fruit = 1
        score += 1

    # move snake
    for i in range(len(snake)):
        past_snake[i][0] = snake[i][0]
        past_snake[i][1] = snake[i][1]

    snake[0][0] += move_speed * move_x
    snake[0][1] += move_speed * move_y

    for i in range(1, len(snake)):
        snake[i][0] = past_snake[i-1][0]
        snake[i][1] = past_snake[i-1][1]

    # check game over
    if snake[0] in snake[1:]:
        print(score)
        start()
    if snake[0][0] <= 25 or snake[0][0] >= 630:
        print(score)
        start()
    if snake[0][1] <= 25 or snake[0][1] >= 630:
        print(score)
        start()

    # draw snake
    for i in range(len(snake)):
        pygame.draw.circle(screen, (0, 0, 0), (snake[i][0], snake[i][1]), 15)

    pygame.display.flip()

print(score)
pygame.quit()
