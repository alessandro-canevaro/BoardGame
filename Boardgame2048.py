try:
    import pygame, os, time
except:
    print('cmd run: pip3 install pygame -i https://mirrors.aliyun.com/pypi/simple')
    exit()
from pygame.locals import *
from components.Game_engine import GameEngine
from components.AI_agent import Agent
from components.Board import *
from test.config import *

# config = Development()
config = SupperFast()

FPS = config.FPS #60
SIZE = config.SIZE #4
colors = config.COLORS
GAME_WH = config.GAME_WH
WINDOW_W = config.WINDOW_W
WINDOW_H = config.WINDOW_H

# font
font_h_w = 2 / 1
g_w = GAME_WH / SIZE * 0.9

class Main():
    def __init__(self):
        global FPS
        pygame.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 50)
        self.set_win_wh(WINDOW_W, WINDOW_H, title='2048')
        self.state = 'start'
        self.fps = FPS
        #self.catch_n = 0
        self.clock = pygame.time.Clock()
        self.game = Board(SIZE)
        #self.ai = Ai()
        self.step_time = config.STEP_TIME
        self.next_f = ''
        self.last_time = time.time()
        self.jm = -1 #evalutation

    def run(self):
        while self.state != 'exit':
            if self.game.state in ['over', 'win']:
                self.state = self.game.state
            self.my_event()
            if self.next_f != '' and (
                    self.state == 'run' or self.state == 'ai' and time.time() - self.last_time > self.step_time):
                self.game.run(self.next_f)
                self.next_f = ''
                self.last_time = time.time()
            elif self.state == 'start':
                self.game.start()
                self.state = 'run'
            self.set_bg((101, 194, 148))
            # self.draw_info()
            # self.draw_button(self.button_list)
            self.draw_map()
            self.update()
        print('退出游戏')

    # 设置窗口大小
    def set_win_wh(self, w, h, title='python游戏'):
        self.screen2 = pygame.display.set_mode((w, h), pygame.DOUBLEBUF, 32)
        self.screen = self.screen2.convert_alpha()
        pygame.display.set_caption(title)

    def set_bg(self, color=(255, 255, 255)):
        self.screen.fill(color)

    def draw_map(self):
        for y in range(SIZE):
            for x in range(SIZE):
                self.draw_block((x, y), self.game.tiles[y][x])
        if self.state == 'over':
            pygame.draw.rect(self.screen, (0, 0, 0, 0.5),
                                    (0, 0, GAME_WH, GAME_WH))
            self.draw_text('Game Over！', (GAME_WH / 2, GAME_WH / 2), size=25, center='center')
        elif self.state == 'win':
            pygame.draw.rect(self.screen, (0, 0, 0, 0.5),
                                    (0, 0, GAME_WH, GAME_WH))
            self.draw_text('Victory！', (GAME_WH / 2, GAME_WH / 2), size=25, center='center')

    # draw block
    def draw_block(self, xy, number):
        one_size = GAME_WH / SIZE
        dx = one_size * 0.05
        x, y = xy[0] * one_size, xy[1] * one_size
        # print(colors[str(int(number))])
        color = colors[str(int(number))] if number <= 2048 else (0, 0, 255)
        pygame.draw.rect(self.screen, color,
                                (x + dx, y + dx, one_size - 2 * dx, one_size - 2 * dx))
        color = (20, 20, 20) if number <= 4 else (250, 250, 250)
        if number != 0:
            ln = len(str(number))
            if ln == 1:
                size = one_size * 1.2 / 2
            elif ln <= 3:
                size = one_size * 1.2 / ln
            else:
                size = one_size * 1.5 / ln

            self.draw_text(str(int(number)), (x + one_size * 0.5, y + one_size * 0.5 - size / 2), color, size, 'center')

    def draw_text(self, text, xy, color=(0, 0, 0), size=18, center=None):
        font = pygame.font.SysFont('simhei', round(size))
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        if center == 'center':
            text_rect.move_ip(xy[0] - text_rect.w // 2, xy[1])
        else:
            text_rect.move_ip(xy[0], xy[1])
        self.screen.blit(text_obj, text_rect)

    def update(self):
        self.screen2.blit(self.screen, (0, 0))
        # update screen
        # pygame.display.update()
        pygame.display.flip()
        time_passed = self.clock.tick(self.fps)