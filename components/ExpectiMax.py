import numpy as np
from components.Board import Board

class Node():
    def __init__(self, parent, board):
        self.parent = parent
        self.children = []
        self.board = board

class MaxNode(Node):
    def __init__(self, parent, board, probability):
        super().__init__(parent, board)
        self.prob = probability

    def Expand(self):
        for m in self.board.PossibleMoves():
            moved_board = Board(self.board)
            moved_board.Swipe(m)
            self.children.append(ChanceNode(self, moved_board, m))

    def ComputeHeuristic(self, depth):
        if depth == 1:
            w_matrix = np.array([[2, 2**2, 2**3, 2**4],
                                [2**8, 2**7, 2**6, 2**5],
                                [2**9, 2**10, 2**11, 2**12],
                                [2**16, 2**15, 2**14, 2**13]])
            return int(np.sum(np.multiply(self.board.values, w_matrix)))

        best_move = self.GetBestMove(depth=depth-1)
        if best_move == 'game_over':
            return 0
        best_child = next((c for c in self.children if c.move == best_move))
        return best_child.GetHeuristic(depth=depth-1)

    def GetBestMove(self, depth):
        if self.children == []:
            self.Expand()
        moves = {c.move: c.GetHeuristic(depth) for c in self.children}
        if moves:
            return max(moves, key=moves.get)
        return 'game_over'

class ChanceNode(Node):
    def __init__(self, parent, board, move):
        super().__init__(parent, board)
        self.move = move

    def Expand(self):
        for pos in self.board.GetEmptyTiles():
            for prob, val in zip([0.9, 0.1], [2, 4]):
                new_board = Board(self.board)
                new_board.SetEmptyTile(pos, val)
                self.children.append(MaxNode(self, new_board, prob))

    def GetHeuristic(self, depth):
        if self.children == []:
            self.Expand()
        """ referencing the paper http://cs229.stanford.edu/proj2016/report/NieHouAn-AIPlays2048-report.pdf"""
        return sum([c.ComputeHeuristic(depth)*c.prob for c in self.children]) / sum([c.prob for c in self.children])

    
class ExpectiMaxAgent:
    def __init__(self, board) -> None:
        self.root = MaxNode(None, board, 1)
        
    def ComputeNextMove(self) -> str:
        return self.root.GetBestMove(depth=2)

    def UpdateTree(self, board):
        self.root = MaxNode(None, board, 1)
    

if __name__ == "__main__":
    print("Do some tests...")
    #b = Board()
    #b.SetEmptyTile((2, 2), 2)
    #print(b)
    #agent = ExpectiMaxAgent()
    #new_board = agent.ExpandTree(b)['l'][4][0]
    #print(new_board)
    #print(agent.ComputeHeuristics(new_board))
    #print(agent.ComputeNextMove(b))
    print("All done")