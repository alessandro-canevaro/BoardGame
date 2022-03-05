import random

import pygame
import numpy as np


red = '#FF0000'
board_size = 4

TILE_COLOR = {2: "red", 4: "green", 8: "blue", 16: "red", 32: "red", 64: "green",
               128: "blue", 256: "red", 512: "green", 1024: "blue", 2048: "red"}

FONT_COLOR = {2: "#FFFFFF", 4: "#FFFFFF", 8: "#FFFFFF", 16: "#FFFFFF",32: "#FFFFFF", 64: "#FFFFFF",
                128: "#FFFFFF", 256: "#FFFFFF", 512: "#FFFFFF", 1024: "#FFFFFF", 2048: "#FFFFFF"}

class MyPygame:
    def __init__(self):
        self.board = np.zeros((4, 4), dtype=int)
        self.screen_w = 400
        self.screen_h = self.screen_w
        self.tile_gap = 10
        pygame.init()
        pygame.display.set_caption("My 2048")

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))

    def get_random_tile_number(self, k=1):
        board_pos = list(zip(*np.where(self.board == 0)))
        for pos in random.sample(board_pos, k=k):
            if random.random() < 0.1:
                self.board[pos] = 4
            else:
                self.board[pos] = 2

    def draw_game(self):
        self.screen.fill(color="gray")

        for i in range(board_size):
            for j in range(board_size):
                temp = self.board[i][j]
                top_left_x = j * self.screen_w // board_size + self.tile_gap
                top_left_y = i * self.screen_h // board_size + self.tile_gap
                tile_w = self.screen_w // board_size - 2 * self.tile_gap
                tile_h = self.screen_h // board_size - 2 * self.tile_gap
                pygame.draw.rect(self.screen, TILE_COLOR[4],
                                 pygame.Rect(top_left_x, top_left_y, tile_w, tile_h), 5)

                if temp == 0:
                    continue
                text_surface = self.myfont.render(f'{temp}', True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(top_left_x + tile_w / 2,
                                                          top_left_y + tile_h / 2))
                self.screen.blit(text_surface, text_rect)

    def _swipeLeft(self, board_values) -> np.ndarray:
        new_board = np.zeros_like(board_values)
        for i in range(self.board_size):
            new_board[i, :] = self._swiperow(board_values[i, :])
        return new_board

    def play(self):
        self.get_random_tile_number(2)
        while True:
            self.draw_game()
            pygame.display.flip()


if __name__ == '__main__':
    game = MyPygame()
    game.play()