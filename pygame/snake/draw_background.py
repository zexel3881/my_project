import pygame

def background(screen):
    pygame.draw.rect(screen, (4,76,7), [0,0,660,660], 30)

    for i in range(0, 10):
        for j in range(0, 10):
            pygame.draw.line(screen, (153, 255, 153), (30 + 60 * j, 44 + i * 60), (60 + 60 * j, 44 + i * 60), 30)
            pygame.draw.line(screen, (102, 204, 102), (60 + 60 * j, 44 + i * 60), (90 + 60 * j, 44 + i * 60), 30)

            pygame.draw.line(screen, (153, 255, 153), (60 + 60 * j, 74 + i * 60), (90 + 60 * j, 74 + i * 60), 30)
            pygame.draw.line(screen, (102, 204, 102), (30 + 60 * j, 74 + i * 60), (60 + 60 * j, 74 + i * 60), 30)