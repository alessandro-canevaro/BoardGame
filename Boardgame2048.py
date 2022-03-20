try:
    import pygame, os, time
except:
    print('cmd run: pip3 install pygame -i https://mirrors.aliyun.com/pypi/simple')
    exit()

'''
pygame setting
Most code references: https://github.com/VacantHusky/2048GameAutoMovePython
'''

from pygame.locals import *
from components.Game_engine import GameEngine
from components.ExpectiMax import ExpectiMaxAgent
from components.MCTStreesearch import MCTSAgent
from components.Board import *
from config import *

# config = Development()
config = SupperFast()

FPS = config.FPS  # 60
SIZE = config.SIZE  # 4
colors = config.COLORS
GAME_WH = config.GAME_WH
WINDOW_W = config.WINDOW_W
WINDOW_H = config.WINDOW_H

# font
font_h_w = 2 / 1
g_w = GAME_WH / SIZE * 0.9


class Main:
    def __init__(self):
        global FPS
        pygame.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 50)
        self.set_win_wh(WINDOW_W, WINDOW_H, title='2048')
        self.state = 'start'
        self.fps = FPS
        self.ai1 = None
        self.ai2 = None
        self.clock = pygame.time.Clock()
        self.game = GameEngine()
        self.step_time = config.STEP_TIME
        self.next_move = ''
        self.last_time = time.time()

    def run(self):
        self.game.start()
        #self.ai = MCTSAgent(self.game.board)
        print(self.next_move)
        self.ai1 = ExpectiMaxAgent(self.game.board, heuristic='snake')
        self.ai2 = MCTSAgent(self.game.board)
        while self.state != 'exit':
            if self.game.state in ['over', 'victory']:
                self.state = self.game.state
            self.my_event()
            if self.next_move != '' and (
                    self.state == 'run' or self.state == 'ai1' or self.state == 'ai2' and time.time() - self.last_time > self.step_time):
                self.game.isGoal()
                self.game.isGameOver()
                self.game.board.Swipe(self.next_move, True)
                self.game.setRandomNumberInTile(k=1)
                self.ai1.UpdateTree(self.game.board, self.next_move)
                self.ai2.UpdateBoard(self.game.board)
                self.next_move = ''
                self.last_time = time.time()
            elif self.state == 'restart':
                self.state = 'run'
                self.run()
            self.set_bg((255, 255, 153))
            self.draw_info()
            self.draw_button(self.button_list)
            self.draw_map()
            self.update()
        #print('Exit game')


    # setting window size
    def set_win_wh(self, w, h, title='2048'):
        self.screen2 = pygame.display.set_mode((w, h), pygame.DOUBLEBUF, 32)
        self.screen = self.screen2.convert_alpha()
        pygame.display.set_caption(title)

    def set_bg(self, color=(153, 255, 204)):
        self.screen.fill(color)

    def draw_map(self):
        for y in range(SIZE):
            for x in range(SIZE):
                self.draw_block((x, y), self.game.board.values[y][x])
        if self.state == 'over':
            pygame.draw.rect(self.screen, (0, 0, 0, 0.5),
                             (0, 0, GAME_WH, GAME_WH))
            self.draw_text('Game Over！', (GAME_WH / 2, GAME_WH / 2), size=25, center='center')
        elif self.state == 'victory':
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

    # event detection
    def my_event(self):
        if self.state == 'ai1' and self.next_move == '':
            self.next_move = self.ai1.ComputeNextMove()
        elif self.state == 'ai2' and self.next_move == '':
            self.next_move = self.ai2.GetNextMove()
        for event in pygame.event.get():
            if event.type == QUIT:
                self.state = 'exit'
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.state = 'exit'
                elif event.key in [K_LEFT, K_a] and self.state == 'run':
                    self.next_move = 'left'
                elif event.key in [K_RIGHT, K_d] and self.state == 'run':
                    self.next_move = 'right'
                elif event.key in [K_DOWN, K_s] and self.state == 'run':
                    self.next_move = 'down'
                elif event.key in [K_UP, K_w] and self.state == 'run':
                    self.next_move = 'up'
                elif event.key in [K_k, K_l] and (self.state == 'ai1' or self.state == 'ai2'):
                    if event.key == K_k and self.step_time > 0:
                        self.step_time *= 0.9
                    if event.key == K_l and self.step_time < 10:
                        if self.step_time != 0:
                            self.step_time *= 1.1
                        else:
                            self.step_time = 0.01
                    if self.step_time < 0:
                        self.step_time = 0

            if event.type == MOUSEBUTTONDOWN:
                for i in self.button_list:
                    if i.is_click(event.pos):
                        self.state = i.player
                        if i.name == 'ai1':
                            i.name = 'run ai1'
                            i.player = 'run'
                            i.text = 'Cancel AI1'
                        elif i.name == 'ai2':
                            i.name = 'run ai2'
                            i.player = 'run'
                            i.text = 'Cancel AI2'
                        elif i.player == 'run' and i.name == 'run ai1':
                            i.name = 'ai1'
                            i.player = 'ai1'
                            i.text = 'ExpectiMax'
                        elif i.player == 'run' and i.name == 'run ai2':
                            i.name = 'ai2'
                            i.player = 'ai2'
                            i.text = 'MCTS'
                        # elif i.player == 'start':
                        #     i.name = 'start'
                        #     i.player = 'start'
                        break

    def draw_info(self):
        self.draw_text('Score：{}'.format(self.game.board.score), (GAME_WH + 50, 40))
        if self.state == 'ai1' or self.state == 'ai2':
            self.draw_text('Step_time：{}'.format(self.step_time), (GAME_WH + 50, 60))
            #self.draw_text('评分：{}'.format(self.jm), (GAME_WH + 50, 80))

    def draw_button(self, buttons):
        for b in buttons:
            if b.is_show:
                pygame.draw.rect(self.screen, (180, 180, 200),
                                 (b.x, b.y, b.w, b.h))
                self.draw_text(b.text, (b.x + b.w / 2, b.y + 9), size=18, center='center')

    def start(self):
        # load button
        self.button_list = [
            Button('start', 'restart', 'Restart', (GAME_WH + 50, 150)),
            Button('ai1', 'ai1', 'ExpectiMax', (GAME_WH + 50, 250)),
            Button('ai2',  'ai2', 'MCTS', (GAME_WH + 50, 350))
        ]
        self.run()


def run():
    Main().start()

# 按钮类
class Button(pygame.sprite.Sprite):
    def __init__(self, name, player, text, xy, size=(100, 50)):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.text = text
        self.player = player
        self.x, self.y = xy[0], xy[1]
        self.w, self.h = size
        self.is_show = True

    def is_click(self, xy):
        return (self.is_show and
                self.x <= xy[0] <= self.x + self.w and
                self.y <= xy[1] <= self.y + self.h)


if __name__ == '__main__':
    run()
