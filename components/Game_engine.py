
import random
import numpy as npy
import copy as cp

board_size = 4
temp_board =[]
class GameEngine:
    def __init__(self):
        #self.board = [[0 for i in range[4]] for j in range [4]]
        self.board = npy.zeros((board_size,board_size))

    def setRandomNumberInTile(self, k=1) ->None: 
        #Trying to get position of the board in the form of (x,y)
        #Here the k will decide how many positions to put random number
        board_position = list(zip(*npy.where(self.board == 0)))
        for rand_pos in random.sample(board_position, k=k):
            if random.randint(1, 8) == 1:
                self.board[rand_pos] = 4
            else:
                self.board[rand_pos] = 2
    #Swipe left        
    def swipeLeft(self,move):
        for i in range(board_size):
            zvalue =  self.board[i, :]
            nvalue = zvalue[zvalue !=0]   
            fvalue = npy.zeros_like(zvalue)
            fvalue[:len(nvalue)] = nvalue
            self.board[i, :] = fvalue
            temp_board = cp.deepcopy(self.board)

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
        """print the whole board in the terminal.
        """
        return self.board
        

    


if __name__ == "__main__":
    ge = GameEngine()
    ge.setRandomNumberInTile(k=2)
    print(ge.printboard())
    ge.swipeLeft(move='l')
    print(ge.printboard())
    #print(ge.TestGoal())
    #ge.board[0][3] = 2048
    #print(ge.TestGoal()
    #print("all done")


