import pygame
from random import randint

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([640, 700])
pygame.display.set_caption('mine_sweeper')
clock = pygame.time.Clock()
FPS = 30  # frame per second
font_1 = pygame.font.SysFont('arrial', 30, False, False)
font_2 = pygame.font.SysFont('arrial', 50, False, False)

# color RGB
color_a = (153, 255, 153)
color_b = (102, 204, 102)
color_c = (229, 194, 159)
color_d = (215, 184, 153)


# first setting
def start():
    global score, mouse_pos, time, cal_time, board, left_mine
    mouse_pos = 0
    click = False
    score = 0
    time = 0
    cal_time = 0
    board = [[0 for i in range(16)] for j in range(16)]
    left_mine = 45


def draw_board():
    for i in range(8):
        for j in range(8):
                pygame.draw.rect(screen, color_a, (0 + 80 * j, 60 + 80 * i, 40, 40))
                pygame.draw.rect(screen, color_b, (40 + 80 * j, 60 + 80 * i, 40, 40))
                pygame.draw.rect(screen, color_b, (0 + 80 * j, 100 + 80 * i, 40, 40))
                pygame.draw.rect(screen, color_a, (40 + 80 * j, 100 + 80 * i, 40, 40))


def draw_brown_board():
    for i in range(16):
        for j in range(16):
            if board[i][j] == 1:
                if i % 2 == j % 2:
                    pygame.draw.rect(screen, color_c, (0 + 40 * i, 60 + 40 * j, 40, 40))
                else:
                    pygame.draw.rect(screen, color_d, (0 + 40 * i, 60 + 40 * j, 40, 40))
            if board[i][j] == 2:
                pygame.draw.circle(screen, (255, 0, 0), (20 + 40 * i, 80 + 40 * j), 15)

screen.fill((255, 255, 255))
start()

time_text = font_1.render("T I M E  :   0", False, (0, 0, 0))

# Run until the user asks to quit
running = True
while running:
    # reset screen
    screen.fill((255, 255, 255))

    clock.tick(FPS)
    draw_board()
    draw_brown_board()

    # calculate time and raw
    cal_time += 1
    if cal_time == FPS:
        time += 1
        cal_time = 0
        time_text = font_1.render("T I M E  :  " + str(time), False, (0, 0, 0))
    screen.blit(time_text, (480, 30))

    # draw how many mines left
    pygame.draw.circle(screen, (255, 0, 0), (280, 33), 20)
    mine_text = font_2.render("  :  " + str(left_mine), False, (0, 0, 0))
    screen.blit(mine_text, (300, 20))

    # 여기서
    pygame.draw.rect(screen, color_c, (80, 60, 40, 40))
    pygame.draw.rect(screen, color_c, (160, 60, 40, 40))
    pygame.draw.rect(screen, color_c, (120, 100, 40, 40))
    pygame.draw.rect(screen, color_d, (120, 60, 40, 40))
    pygame.draw.rect(screen, color_d, (80, 100, 40, 40))
    pygame.draw.rect(screen, color_d, (160, 100, 40, 40))

    pygame.draw.lines(screen, (0, 0, 0), True, [[80, 60], [200, 60], [200, 140], [80, 140]], 2)
    #여까지 지워

    for event in pygame.event.get():
        # check is there mouse_input?
        if event.type == pygame.MOUSEBUTTONUP:
            # left click
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = [mouse_pos[0] // 40, (mouse_pos[1] - 60) // 40]
                if board[mouse_pos[0]][mouse_pos[1]] == 2:
                    left_mine += 1
                board[mouse_pos[0]][mouse_pos[1]] = 1

            # right click
            elif event.button == 3:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = [mouse_pos[0] // 40, (mouse_pos[1] - 60) // 40]

                if board[mouse_pos[0]][mouse_pos[1]] == 0:
                    board[mouse_pos[0]][mouse_pos[1]] = 2
                    left_mine -= 1

                elif board[mouse_pos[0]][mouse_pos[1]] == 2:
                    board[mouse_pos[0]][mouse_pos[1]] = 0
                    left_mine += 1

        # when you clik quit out button, this code make you go out
        if event.type == pygame.QUIT:
            running = False
            break

    pygame.display.flip()


print(score)
pygame.quit()