import pygame as pg
import numpy as np
import sys
from math import *

FPS = 200
class dice:
    def __init__(self, x, y):
        self.t = pi/4
        self.u = pi/4
        self.x = x
        self.y = y

        self.pos = np.array([
            [x-30, y-30], [x-30, y+30], [x+30, y+30], [x+30, y-30],
            [x-30, y-30], [x-30, y+30], [x+30, y+30], [x+30, y-30],
                ])

        self.number = 1

    def rotate(self):
        self.t += 2 / FPS
        self.u += 2 / FPS
        cc = sqrt(cos(self.t)**2 + cos(self.u)**2)

        self.pos = np.array([
            [self.x - 30 * cos(self.t), self.y - 30 * cos(self.u)], [self.x - 30 * cos(self.t), self.y + 30 * sin(self.u)],
            [self.x + 30 * sin(self.t), self.y + 30 * sin(self.u)], [self.x + 30 * sin(self.t), self.y - 30 * cos(self.u)],
            [self.x - 30 * sin(self.t), self.y - 30 * sin(self.u)], [self.x - 30 * sin(self.t), self.y + 30 * cos(self.u)],
            [self.x + 30 * cos(self.t), self.y + 30 * cos(self.u)], [self.x + 30 * cos(self.t), self.y - 30 * sin(self.u)],
        ])

class game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([700, 700])
        pg.display.set_caption('dice')

        self.dice1 = dice(100, 100)

    def new_game(self):
        self.dice1 = dice(100, 100)

    def draw(self):
        self.screen.fill('black')
        # pg.draw.lines(self.screen, 'white', True, self.dice1.pos[:4], 3)
        # pg.draw.lines(self.screen, 'white', True, self.dice1.pos[5:9], 3)

        [pg.draw.circle(self.screen, 'yellow', i, 3) for i in self.dice1.pos[4:9]]
        [pg.draw.circle(self.screen,'white', i, 3) for i in self.dice1.pos[:4]]


    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.new_game()


    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)

    def run(self):
        while True:
            self.update()
            self.draw()
            self.dice1.rotate()
            self.check_event()


if __name__ == '__main__':
    game = game()
    game.run()