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
            moved_board.Swipe(m, False)
            self.children.append(ChanceNode(self, moved_board, m))

    def HeuristicSnake(self, board):
        weights = np.exp2(np.array([[1,  2,  3,  4],
                                    [8,  7,  6,  5], 
                                    [9,  10, 11, 12], 
                                    [16, 15, 14, 13]]))
        return np.sum(np.multiply(board, weights))

    def HeuristicEmptySnake(self, board):
        weights = np.exp2(np.array([[1,  2,  3,  4],
                                    [8,  7,  6,  5], 
                                    [9,  10, 11, 12], 
                                    [16, 15, 14, 13]]))
        boost = (np.count_nonzero(board==0)/1)+1
        return np.sum(np.multiply(board, weights)) * boost

    def HeuristicSnake8x(self, board):
        weights = np.exp2(np.array([[1,  2,  3,  4],
                                    [8,  7,  6,  5], 
                                    [9,  10, 11, 12], 
                                    [16, 15, 14, 13]]))
        results = []
        for i in range(4):
            rotated = np.rot90(weights, i)
            results.append(np.sum(np.multiply(board, rotated)))
            results.append(np.sum(np.multiply(board, np.fliplr(rotated))))
        return max(results)
            
    def ComputeHeuristic(self, depth, heuristic='snake'):
        if depth == 1:
            h_func = {'snake': self.HeuristicSnake,
                      'emptysnake': self.HeuristicEmptySnake,
                      'snake8x': self.HeuristicSnake8x}[heuristic]
            return h_func(self.board.values)

        best_move = self.GetBestMove(depth-1, heuristic)
        if best_move == 'game_over':
            return 0
        best_child = next((c for c in self.children if c.move == best_move))
        return best_child.GetHeuristic(depth-1, heuristic)

    def GetBestMove(self, depth, heuristic):
        if self.children == []:
            self.Expand()

        moves = {c.move: c.GetHeuristic(depth, heuristic) for c in self.children}
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

    def GetHeuristic(self, depth, heuristic):
        if self.children == []:
            self.Expand()
        """ referencing the paper http://cs229.stanford.edu/proj2016/report/NieHouAn-AIPlays2048-report.pdf"""
        return sum([c.ComputeHeuristic(depth, heuristic)*c.prob for c in self.children]) / sum([c.prob for c in self.children])

    
class ExpectiMaxAgent:
    def __init__(self, board, depth='adaptive', heuristic='snake') -> None:
        self.root = MaxNode(None, board, 1)
        self.depth = depth
        self.heuristic = heuristic
        
    def ComputeNextMove(self) -> str:
        if self.depth=='adaptive':
            empty_tiles = len(self.root.board.GetEmptyTiles())
            if empty_tiles > 8:
                depth = 1
            elif empty_tiles > 2:
                depth = 2
            else:    
                depth = 3
        else:
            depth = self.depth

        return self.root.GetBestMove(depth, self.heuristic)

    def UpdateTree(self, board, lastmove):
        best_child = next((c for c in self.root.children if c.move == lastmove), None)
        if best_child != None:
            for c in best_child.children:
                if c.board == board:
                    self.root = c
        else:
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