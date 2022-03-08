import random
from components.Board import Board

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
        print(self.board)
        