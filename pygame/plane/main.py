import pygame
import sys
import random
import time

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((630, 910))
pygame.display.set_caption('asd')
white = (255,255,255)
black = (0, 0, 0)
yellow = (255, 200, 0)
asd = (0, 0, 255)
red = (255, 0, 0)

playing = 1

plane_x = 315
x_level = 3
plane_y = 805

bullet = []
boss_xy = []
enemy = []
spawn_enemy_time = 0
score = 0

while playing:
    clock.tick(250)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(score)
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x_level != 1:
                    plane_x -= 120
                    x_level -= 1
            elif event.key == pygame.K_RIGHT:
                if x_level != 5:
                    plane_x += 120
                    x_level += 1
            elif event.key == pygame.K_SPACE:
                bullet.append([plane_x,plane_y-60])

    pygame.draw.circle(screen, white, (plane_x, plane_y), 50)

    if len(bullet) != 0:
        for i in range(len(bullet)):
            bullet[i][1] -= 10
        if bullet[0][1] == 5:
            del bullet[0]
    for i in bullet:
        pygame.draw.circle(screen, yellow, (i[0],i[1]), 10)

    spawn_enemy_time += 1
    boss = 0
    if spawn_enemy_time == 100:
        boss = random.randrange(1,6)
        if boss == 1:
            enemy.append([[195, 0],[315, 0],[435, 0],[555, 0]])
            boss_xy.append([75, 0])
        elif boss == 2:
            enemy.append([[75, 0],[315, 0],[435, 0],[555, 0]])
            boss_xy.append([195, 0])
        elif boss == 3:
            enemy.append([[75, 0],[195, 0],[435, 0],[555, 0]])
            boss_xy.append([315, 0])
        elif boss == 4:
            enemy.append([[75, 0],[195, 0],[315, 0],[555, 0]])
            boss_xy.append([435, 0])
        elif boss == 5:
            enemy.append([[75, 0],[195, 0],[315, 0],[435, 0]])
            boss_xy.append([555, 0])
        spawn_enemy_time = 0

    for i in range(len(boss_xy)):
        boss_xy[i][1] += 5
        enemy[i][0][1] += 5
        enemy[i][1][1] += 5
        enemy[i][2][1] += 5
        enemy[i][3][1] += 5
        if boss_xy[0][1] == 755:
            pygame.quit()
            print(score)


    if len(bullet) != 0 and len(boss_xy) != 0:
        if (bullet[0][1] - boss_xy[0][1]) <= 5:
            if bullet[0][0] == boss_xy[0][0]:
                del boss_xy[0]
                del enemy[0]
                del bullet[0]
                score += 1
            else:
                del bullet[0]

    for i in boss_xy:
        pygame.draw.circle(screen, red, (i[0],i[1]), 50)
    for i in enemy:
        pygame.draw.circle(screen, asd, (i[0][0],i[0][1]), 45)
        pygame.draw.circle(screen, asd, (i[1][0],i[1][1]), 45)
        pygame.draw.circle(screen, asd, (i[2][0],i[2][1]), 45)
        pygame.draw.circle(screen, asd, (i[3][0],i[3][1]), 45)

    pygame.display.flip()