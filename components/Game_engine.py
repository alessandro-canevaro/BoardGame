import random
from components.Board import Board
import numpy as np

class GameEngine:
    def __init__(self):
        self.board = Board()

    def setRandomNumberInTile(self, k=1) ->None: 
        """Add k random new tiles in the empty positions of the board.
        """
        #Trying to get position of the board in the form of (x,y)
        #Here the k will decide how many positions to put random number
        board_positions = self.board.GetEmptyTiles()
        if len(board_positions) >= k:
            rand_pos = random.sample(board_positions, k=k)
            rand_num = random.choices([2, 4], [0.9, 0.1], k=k)
            for pos, value in zip(rand_pos, rand_num):
                self.board.SetEmptyTile(pos, value)
                
    # checking board is same or not
    def isSameBoard(self)-> bool:
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
        board_list=[]
        print(list(self.board.values))
        for j in range(4):
            row = self.board.values[j]
            board_list = np.append(board_list, row)
        max_num_width = len(str(max(board_list)))
        conver2char = lambda num: '{0:>{1}}'.format(num, max_num_width) \
            if num > 0 else ' ' * max_num_width
        demarcation = ('+' + '-' * (max_num_width + 2)) * 4 + '+'  # generate demarcation line like '+---+---+---+'
        print(demarcation)
        for i in range(4):
            print((demarcation + '\n').join(['| ' + ' | '.join([conver2char(int(num)) for num in board_list[i * 4:(i + 1) * 4]]) + ' | ']))
            print(demarcation)