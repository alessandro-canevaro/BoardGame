import random
import sys

import pygame
import numpy as np
from pygame.locals import *
from components.Board import Board

class GameEngine:
    state = 'start'
    def __init__(self):
        self.board = Board()
        
        
    def start(self, k=2) -> None:
        self.board = Board()
        self.setRandomNumberInTile(k)
        self.state = 'run'

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
        return None

    # checking board is same or not
    def isSameBoard(self) -> bool:
        if temp_board == self.board:
            return True

    def isGameOver(self) -> bool:
        if self.board.PossibleMoves():
            return False
        self.state = 'over'
        return True

    def isGoal(self, goal=2048) -> bool:
        """Return True if the board contains the goal value.
        """
        if any(goal in row for row in self.board):
            self.state = 'victory'
            return True
        return False

    def printBoard(self):
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
            print((demarcation + '\n').join(['| ' + ' | '.join([conver2char(int(num)) for num in board_list[i * 4:(i + 1) * 4]]) + ' | ']))
            print(demarcation)

    
if __name__ == "__main__":
    ge = GameEngine()
    ge.setRandomNumberInTile(k=2)
    print(ge.board.values[0][1])
    print((demarcation + '\n').join(['| ' + ' | '.join(
                [conver2char(int(num)) for num in board_list[i * 4:(i + 1) * 4]]) + ' | ']))
    print(demarcation)


    
    

