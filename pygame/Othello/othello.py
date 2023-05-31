import pygame as pg
import sys

color_a = (153, 255, 153)
color_b = (102, 204, 102)
delta = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

class Map:
    def __init__(self, game):
        self.game = game
        self.board = [
            [7,  7,  7,  7,  7,  7,  7,  7,  7, 7],
            [7, -1, -1, -1, -1, -1, -1, -1, -1, 7],
            [7, -1, -1, -1, -1, -1, -1, -1, -1, 7],
            [7, -1, -1, -1, -1, -1, -1, -1, -1, 7],
            [7, -1, -1, -1,  0,  1, -1, -1, -1, 7],
            [7, -1, -1, -1,  1,  0, -1, -1, -1, 7],
            [7, -1, -1, -1, -1, -1, -1, -1, -1, 7],
            [7, -1, -1, -1, -1, -1, -1, -1, -1, 7],
            [7, -1, -1, -1, -1, -1, -1, -1, -1, 7],
            [7,  7,  7,  7,  7,  7,  7,  7,  7, 7]
        ]

    def draw_board(self):
        if not self.game.turn:
            self.game.screen.fill('black')
        else:
            self.game.screen.fill('white')

        for i in range(4):
            for j in range(4):
                pg.draw.rect(self.game.screen, color_a, (0 + 140 * j, 140 * i, 70, 70))
                pg.draw.rect(self.game.screen, color_b, (70 + 140 * j, 140 * i, 70, 70))
                pg.draw.rect(self.game.screen, color_b, (0 + 140 * j, 70 + 140 * i, 70, 70))
                pg.draw.rect(self.game.screen, color_a, (70 + 140 * j, 70 + 140 * i, 70, 70))

    def draw_dot(self):
        for i in range(8):
            for j in range(8):
                if self.board[i+1][j+1] == 0:
                    pg.draw.circle(self.game.screen, 'black',[i * 70 + 35, j * 70 + 35] ,30)
                elif self.board[i+1][j+1] == 1:
                    pg.draw.circle(self.game.screen, 'white',[i * 70 + 35, j * 70 + 35] ,30)


class game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([560, 595])
        pg.display.set_caption('othello')
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.who_win = -1
        self.hmm = 0
        self.turn = False

    def update(self):
        pg.display.flip()
        self.clock.tick(30)

    def check_can_put(self, pos, change):
        can_or_not = False
        for i in range(8):
            x, y = pos[0], pos[1]
            if self.map.board[x][y] != -1:
                continue

            dx, dy = delta[i]
            change_list = []

            while True:
                x += dx
                y += dy
                k = self.map.board[x][y]

                if k == 7 or k == -1:
                    change_list = []
                    break
                if k == int(self.turn):
                    break
                else:
                    change_list.append([x, y])

            if change_list:
                can_or_not = True
            if change:
                for j in change_list:
                    self.map.board[j[0]][j[1]] = int(self.turn)

        return can_or_not

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                self.mouse_pos = pg.mouse.get_pos()
                self.mouse_pos = [self.mouse_pos[0] // 70 + 1, self.mouse_pos[1] // 70 + 1]

                if self.check_can_put(self.mouse_pos, True):
                    self.map.board[self.mouse_pos[0]][self.mouse_pos[1]] = int(self.turn)
                    self.turn = not self.turn

                self.who_win = self.check_end()
                if self.who_win != -1:
                    print(self.who_win)

            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.new_game()

    def check_end(self):
        for i in range(1, 9):
            for j in range(1, 9):
                k = self.check_can_put([i, j], False)
                if k:
                    self.hmm = 0
                    return -1

        if self.hmm == 0:
            self.hmm += 1
            self.turn = not self.turn
            self.map.draw_board()
            self.map.draw_dot()

        N = [0, 0]
        for i in self.map.board[1:-1]:
            N[0] += i.count(0)
            N[1] += i.count(1)

        if N[0] == 0 or N[1] == 0:
            return N.index(max(N))
        if sum(N) == 64:
            return N.index(max(N))
        if self.hmm == 1:
            return N.index(max(N))

        return -1

    def check_remain(self):
        pass

    def run(self):
        while True:
            self.check_event()
            self.check_remain()
            self.map.draw_board()
            self.map.draw_dot()
            self.update()

if __name__ == '__main__':
    game = game()
    game.run()