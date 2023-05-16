import pygame
from random import randint

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([640, 700])
pygame.display.set_caption('mine_sweeper')
clock = pygame.time.Clock()
FPS = 100  # frame per second
font_1 = pygame.font.SysFont('arrial', 30)
font_2 = pygame.font.SysFont('arrial', 50)
number_font = pygame.font.SysFont('script', 40)

# color RGB
color_a = (153, 255, 153)
color_b = (102, 204, 102)
color_c = (229, 194, 159)
color_d = (215, 184, 153)


# first setting
def start():
    global score, mouse_pos, time, cal_time, board, left_mine, where_mine
    global mine_zero, number_mine, is_first, board_for_check

    mouse_pos = 0
    click = False
    score = 0
    time = 0
    cal_time = 0
    board = [[0 for i in range(18)] for j in range(18)]
    board_for_check = [[-1,-1, -1, -1, -1, -1, -1,-1, -1, -1, -1, -1, -1,-1, -1, -1, -1, -1]] + [[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1] for i in range(16)] + [[-1,-1, -1, -1, -1, -1, -1,-1, -1, -1, -1, -1, -1,-1, -1, -1, -1, -1]]
    where_mine = [[0 for i in range(18)] for j in range(18)]
    number_mine = [[0 for i in range(18)] for j in range(18)]
    left_mine = 45
    is_first = True
    mine_zero = []


# make green part
def draw_board():
    for i in range(8):
        for j in range(8):
                pygame.draw.rect(screen, color_a, (0 + 80 * j, 60 + 80 * i, 40, 40))
                pygame.draw.rect(screen, color_b, (40 + 80 * j, 60 + 80 * i, 40, 40))
                pygame.draw.rect(screen, color_b, (0 + 80 * j, 100 + 80 * i, 40, 40))
                pygame.draw.rect(screen, color_a, (40 + 80 * j, 100 + 80 * i, 40, 40))


# make brown part and number
def draw_brown_board():
    for i in range(16):
        for j in range(16):
            if board[j+1][i+1] == 1:
                if i % 2 == j % 2:
                    pygame.draw.rect(screen, color_c, (0 + 40 * i, 60 + 40 * j, 40, 40))
                else:
                    pygame.draw.rect(screen, color_d, (0 + 40 * i, 60 + 40 * j, 40, 40))

                if number_mine[j + 1][i + 1] != 0:
                    number_text = number_font.render(str(number_mine[j + 1][i + 1]), False, (0, 0, 0))
                    screen.blit(number_text, (10 + 40 * i, 55 + 40 * j))

            if board[j+1][i+1] == 2:
                pygame.draw.circle(screen, (255, 0, 0), (20 + 40 * i, 80 + 40 * j), 15)


def set_mine(never_this):
    a = (never_this[0]-1) + 16*(never_this[1]-1) + 1

    where_mine[never_this[1]][never_this[0]] = '@'
    a = [a, a-1, a+1, a-17, a-16, a - 15, a + 16, a + 17, a + 15]
    mine = []
    c = 0

    # choice position of mine execpt first open position and near
    while c < left_mine:
        b = randint(1, 256)

        if b not in mine and b not in a:
            mine.append(b)
            c += 1

    print(len(mine))

    for i in mine:
        p = i//16+ 1  # 열
        q = i % 16  # 행
        if q == 0:
            p -= 1
            q = 16
        where_mine[p][q] = 1

        number_mine[p - 1][q - 1] += 1
        number_mine[p][q - 1] += 1
        number_mine[p + 1][q - 1] += 1
        number_mine[p - 1][q] += 1
        number_mine[p][q] += 1
        number_mine[p + 1][q] += 1
        number_mine[p - 1][q + 1] += 1
        number_mine[p][q + 1] += 1
        number_mine[p + 1][q + 1] += 1

    for i in range(1, 17):
        for j in range(1, 17):
            if number_mine[i][j] == 0:
                mine_zero.append((i-1) * 16 + j)


def cover_zero_board(pos):
    if board_for_check[pos[1]][pos[0]] == 0:
        board[pos[1] - 1][pos[0] - 1] = 1
        board[pos[1] - 1][pos[0]] = 1
        board[pos[1] - 1][pos[0] + 1] = 1
        board[pos[1]][pos[0] - 1] = 1
        board[pos[1]][pos[0] + 1] = 1
        board[pos[1] + 1][pos[0] - 1] = 1
        board[pos[1] + 1][pos[0]] = 1
        board[pos[1] + 1][pos[0] + 1] = 1

        board_for_check[pos[1]][pos[0]] = 1


screen.fill((255, 255, 255))
start()

time_text = font_1.render("T I M E  :   0", False, (0, 0, 0))

# Run until the user asks to quit
running = True
while running:
    clock.tick(FPS)

    # reset screen
    screen.fill((255, 255, 255))

    # draw board
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

    for event in pygame.event.get():
        # check is there mouse_input?
        if event.type == pygame.MOUSEBUTTONUP:

            # left click
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = [mouse_pos[0] // 40 + 1, (mouse_pos[1] - 60) // 40 + 1]

                if board[mouse_pos[1]][mouse_pos[0]] == 2:
                    left_mine += 1

                board[mouse_pos[1]][mouse_pos[0]] = 1

                if is_first:
                    set_mine(mouse_pos)
                    is_first = False
                    print()
                    for i in range(1, len(number_mine) - 1):
                        print(*where_mine[i][1:17], end='             ')
                        print(*board[i][1:17], end='             ')
                        print(*number_mine[i][1:17])

                # 지뢰 밟았다!
                elif where_mine[mouse_pos[1]][mouse_pos[0]] == 1:
                    number_mine[mouse_pos[1]][mouse_pos[0]] = '!'


                if number_mine[mouse_pos[1]][mouse_pos[0]] == 0:
                    cover_zero_board(mouse_pos)

            # right click
            elif event.button == 3 and not is_first:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = [mouse_pos[0] // 40 + 1, (mouse_pos[1] - 60) // 40 + 1]

                if board[mouse_pos[1]][mouse_pos[0]] == 0:
                    board[mouse_pos[1]][mouse_pos[0]] = 2
                    left_mine -= 1

                elif board[mouse_pos[1]][mouse_pos[0]] == 2:
                    board[mouse_pos[1]][mouse_pos[0]] = 0
                    left_mine += 1


        for i in mine_zero:
            a = i // 16 + 1
            b = i % 16

            if board[a][b] == 1:
                cover_zero_board(([b, a]))

        # when you clik quit out button, this code make you go out
        if event.type == pygame.QUIT:
            running = False
            break

    pygame.display.flip()


print(score)
pygame.quit()
