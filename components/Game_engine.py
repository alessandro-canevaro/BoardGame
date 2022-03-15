import random
import sys

import pygame
import numpy as np
from pygame.locals import *
from components.Board import Board

board_size = 4

TILE_COLOR = {2: "#EDE4DA", 4: "#EDDFC9",  8: "#F2B178", 16: "#F59563", 32: "#F67C5F", 64: "#F65D3B",
              128: "#EDCF72", 256: "#EECC61", 512: "#EDC751", 1024: "#EEC43F", 2048: "#edc22e", 4096: "#3c3a32"}

FONT_COLOR = {2: "#766E65", 4: "#766E65", 8: "#F8F6F2", 16: "#F8F6F2", 32: "#F8F6F2", 64: "#F8F6F2",
              128: "#F8F6F2", 256: "#F8F6F2", 512: "#F8F6F2", 1024: "#F8F6F2", 2048: "#F8F6F2", 4096: "#F8F6F2"}
BG_COLOR = '#BBAD9F'
NV_COLOR = '#CCC1B4'


class GameEngine:
    def __init__(self):
        self.board = Board()
        self.screen_w = 400
        self.screen_h = self.screen_w
        self.tile_gap = 10
        pygame.init()
        pygame.display.set_caption("AI-BoardGame 2048")
        pygame.font.init()
        self.primary_font = pygame.font.SysFont('Comic Sans MS', 36)
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))

    def setRandomNumberInTile(self, k=1) -> None:
        """Add k random new tiles in the empty positions of the board.
        """
        # Trying to get position of the board in the form of (x,y)
        # Here the k will decide how many positions to put random number
        board_positions = self.board.GetEmptyTiles()
        if len(board_positions) >= k:
            rand_pos = random.sample(board_positions, k=k)
            rand_num = random.choices([2, 4], [0.9, 0.1], k=k)
            for pos, value in zip(rand_pos, rand_num):
                self.board.SetEmptyTile(pos, value)

    # checking board is same or not
    def isSameBoard(self) -> bool:
        if temp_board == self.board:
            return True

    def isGameOver(self) -> bool:
        if self.board.PossibleMoves():
            return False
        return True

    def isGoal(self, goal=2048) -> bool:
        """Return True if the board contains the goal value.
        """
        return any(goal in row for row in self.board)

    def printboard(self):
        """
        print the board.
        """
        board_list = []
        # print(list(self.board.values))
        for j in range(4):
            row = self.board.values[j]
            board_list = np.append(board_list, row)
        max_num_width = len(str(max(board_list)))

        def conver2char(num): return '{0:>{1}}'.format(num, max_num_width) \
            if num > 0 else ' ' * max_num_width
        # generate demarcation line like '+---+---+---+'
        demarcation = ('+' + '-' * (max_num_width + 2)) * 4 + '+'
        print(demarcation)
        for i in range(4):
            print((demarcation + '\n').join(['| ' + ' | '.join(
                [conver2char(int(num)) for num in board_list[i * 4:(i + 1) * 4]]) + ' | ']))
            print(demarcation)


    """ Graphicl representation of the game """
    def draw_game(self):
        self.screen.fill(BG_COLOR)

        for i in range(board_size):
            for j in range(board_size):
                temp = self.board.values[i][j]
                top_left_x = j * self.screen_w // board_size + self.tile_gap
                top_left_y = i * self.screen_h // board_size + self.tile_gap
                tile_w = self.screen_w // board_size - 2 * self.tile_gap
                tile_h = self.screen_h // board_size - 2 * self.tile_gap

                if temp == 0:
                    pygame.draw.rect(self.screen, NV_COLOR,
                                    pygame.Rect(top_left_x, top_left_y, tile_w, tile_h))
                    pygame.display.flip()
                    # continue
                elif temp > 2048:
                    pygame.draw.rect()
                    pygame.draw.rect(self.screen, TILE_COLOR[4096],
                                    pygame.Rect(top_left_x, top_left_y, tile_w, tile_h))
                    text = self.primary_font.render(
                        f'{temp}', True, FONT_COLOR[4096])
                    text_pos = text.get_rect(
                        center=(top_left_x + tile_w / 2, top_left_y + tile_h / 2))
                    self.screen.blit(text, text_pos)
                    pygame.display.flip()

                else:
                    pygame.draw.rect(self.screen, TILE_COLOR[temp],
                                    pygame.Rect(top_left_x, top_left_y, tile_w, tile_h))
                    text = self.primary_font.render(
                        f'{temp}', True, FONT_COLOR[2])
                    text_pos = text.get_rect(
                        center=(top_left_x + tile_w / 2, top_left_y + tile_h / 2))
                    self.screen.blit(text, text_pos)
                    pygame.display.flip()


    def key_press(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return 'q'
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        return 'u'
                    elif event.key == K_RIGHT:
                        return 'r'
                    elif event.key == K_LEFT:
                        return 'l'
                    elif event.key == K_DOWN:
                        return 'd'
                    elif event.key == K_q or event.key == K_ESCAPE:
                        return 'q'
    
    def auto_play(self):
        #clock = pygame.time.Clock()
        self.draw_game()
        while pygame.event.get():
            self.draw_game()
            pygame.display.flip()

        """while True:
            self.draw_game()
            pygame.display.flip()
            cmd = key_press()
            if cmd == 'l':
                board = self.swipe_left(self.board)
                self.board = board
            elif cmd == 'q':
                break"""
