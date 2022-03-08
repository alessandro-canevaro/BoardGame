import numpy as np
from components.Board import Board


class ExpectiMaxAgent:
    def __init__(self) -> None:
        self.w_matrix = np.array([[2, 2**2, 2**3, 2**4],
        [2**8, 2**7, 2**6, 2**5],
        [2**9, 2**10, 2**11, 2**12],
        [2**16, 2**15, 2**14, 2**13]
        ])
        

    def ExpandTree(self, board) -> dict:
        """For each possible move generate all the possible boards with one new tile"""
        boards_dict = {}
        possible_moves = board.PossibleMoves()
        for m in board.PossibleMoves():
            moved_board = Board(board)
            moved_board.Swipe(m)
            boards_dict[m] = {2: [], 4: []}
            for pos in moved_board.GetEmptyTiles():
                boards_dict[m][2].append(Board(moved_board))
                boards_dict[m][2][-1].SetEmptyTile(pos, 2)
                boards_dict[m][4].append(Board(moved_board))
                boards_dict[m][4][-1].SetEmptyTile(pos, 4)

        return boards_dict

    def ComputeHeuristics(self, board) -> int:
        """ referencing the paper http://cs229.stanford.edu/proj2016/report/NieHouAn-AIPlays2048-report.pdf"""
        return int(np.sum(np.multiply(board.values, self.w_matrix)))

    def ComputeNextMove(self, board) -> str:
        moves_dict = self.ExpandTree(board)
        for move, boards_dict in moves_dict.items():
            for num, boards_list in boards_dict.items():
                moves_dict[move][num] = np.mean([self.ComputeHeuristics(b) for b in boards_list])
            moves_dict[move] = 0.9*moves_dict[move][2]+0.1*moves_dict[move][4]
        return max(moves_dict, key=moves_dict.get)
    

if __name__ == "__main__":
    print("Do some tests...")
    b = Board()
    b.SetEmptyTile((2, 2), 2)
    print(b)
    agent = ExpectiMaxAgent()
    new_board = agent.ExpandTree(b)['l'][4][0]
    print(new_board)
    print(agent.ComputeHeuristics(new_board))
    print(agent.ComputeNextMove(b))
    print("All done")