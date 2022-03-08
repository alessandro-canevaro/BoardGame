class Agent:
    def __init__(self) -> None:
        self.w_matrix = [[2, 2**2, 2**3, 2**4],
        [2**8, 2**7, 2**6, 2**5],
        [2**9, 2**10, 2**11, 2**12],
        [2**16, 2**15, 2**14, 2**13]
        ]
        

    def ExpandTree(self) -> None:
        pass

    def ComputeHeuristics(self, board):
        """ referencing the paper http://cs229.stanford.edu/proj2016/report/NieHouAn-AIPlays2048-report.pdf"""
        hval = 0
        for i in range(4):
            for j in range(4):
                hval =  hval+ board[i][j] * self.w_matrix[i][j]
            
        return hval

    def ComputeNextMove(self) -> int:
        return Moves.up
    
    def ComputeExpectimax(self, board, depth):
        if depth == 0:
            return self.ComputeHeuristics(board)
        elif depth == 1:
            ''' chance node '''
            ''' to do something'''
            return self.ComputeExpectimax(board,depth-1)
        else:
             pass


            

        
class Moves:
    up = 0
    down = 1
    left = 2
    right = 3

if __name__ == "__main__":
    print("Do some tests...")
    agent = Agent()
    print(agent.ComputeNextMove())
    print("All done")