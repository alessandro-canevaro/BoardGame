
import random
import numpy as np
import copy as cp

board_size = 4
temp_board =[]
class GameEngine:
    def __init__(self):
        #self.board = [[0 for i in range[4]] for j in range [4]]
        self.board = np.zeros((board_size,board_size))

    def setRandomNumberInTile(self, k=1) ->None: 
        #Trying to get position of the board in the form of (x,y)
        #Here the k will decide how many positions to put random number
        board_position = list(zip(*np.where(self.board == 0)))
        for rand_pos in random.sample(board_position, k=k):
            if random.randint(1, 8) == 1:
                self.board[rand_pos] = 4
            else:
                self.board[rand_pos] = 2

    def _compress(self, row):
        """compress all the numbers on one side of the board.
        """
        new_row = [i for i in row if i != 0]
        return new_row + [0] * (4-len(new_row))

    def _swiperow(self, row):
        """return the row after a swipe from right to left.
        """
        row = self._compress(row)
        for i in range(len(row)-1):
            if row[i] == row[i+1]:
                row[i] = row[i]*2
                row[i+1] = 0
        return self._compress(row)

    #Swipe left  
    def swipeLeft(self):
        for i in range(4):
            self.board[i, :] = self._swiperow(self.board[i, :])

        #for i in range(board_size):
        #    zvalue =  self.board[i, :]
        #    nvalue = zvalue[zvalue !=0]   
        #    fvalue = np.zeros_like(zvalue)
        #    fvalue[:len(nvalue)] = nvalue
        #    self.board[i, :] = fvalue
        #    temp_board = cp.deepcopy(self.board)

            # merging while swiping left

    #Swipe Right  
    def swipeRight(self, move):
        pass
    
    #Swipe Down
    def swipeDown(self, move):
            pass

    #Swipe Up
    def swipeUp(self, move):
        pass
    
    # checking board is same or not
    def isSameBoard(self)-> bool:
        if temp_board == self.board:
            return True
    
    def isGameOver(self) -> bool:
        if self.isNoMove() == True:
            return True
        
    
    def isNoMove(self) -> bool:
        #check all 4 way merge, if board return same then no more move.
        pass

    def TestGoal(self, goal=2048) -> bool:
        """Return True if the board contains the goal value.
        """
        return any(goal in row for row in self.board)

    def SpawnNumber(self, value=2) -> None:
        """Add 'value' in an empty tile of the board randomly.
        """
        pass
    def printboard(self):
        return self.board
        

    


if __name__ == "__main__":
    ge = GameEngine()
    ge.setRandomNumberInTile(k=2)
    print(ge.printboard())
    ge.swipeLeft()
    print(ge.printboard())
    #print(ge.TestGoal())
    #ge.board[0][3] = 2048
    #print(ge.TestGoal()
    #print("all done")


